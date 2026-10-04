from flask import Flask, request, render_template, redirect, make_response
import sqlite3
import os
import requests
import jwt

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ---------------- DATABASE ----------------
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    c.execute("INSERT INTO users VALUES ('admin', 'admin123')")
    conn.commit()
    conn.close()

init_db()

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('index.html')

# ---------------- SQL INJECTION ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # VULNERABLE QUERY
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        result = c.execute(query).fetchone()

        if result:
            resp = make_response(redirect('/dashboard'))
            resp.set_cookie('role', 'user')
            return resp

    return render_template('login.html')

# ---------------- COOKIE MANIPULATION ----------------
@app.route('/dashboard')
def dashboard():
    role = request.cookies.get('role')

    if role == 'admin':
        return "CTF{cookie_admin_access}"
    return "Welcome normal user"

# ---------------- HIDDEN ROUTE ----------------
@app.route('/super-secret-admin-panel-xyz')
def hidden():
    return "CTF{hidden_directory_found}"

# ---------------- XSS ----------------
comments = []

@app.route('/comments', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        user_input = request.form['comment']
        comments.append(user_input)

    return render_template('comments.html', comments=comments)

# ---------------- FILE UPLOAD ----------------
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return f"Uploaded: /uploads/{file.filename}"

    return '''
    <form method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit">
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return open(os.path.join(UPLOAD_FOLDER, filename)).read()

# ---------------- SSRF ----------------
@app.route('/fetch')
def fetch():
    url = request.args.get('url')
    return requests.get(url).text

# ---------------- IDOR ----------------
@app.route('/profile')
def profile():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    data = c.execute(f"SELECT username FROM users WHERE rowid={user_id}").fetchone()
    return f"User: {data[0]}"

# ---------------- COMMAND INJECTION ----------------
@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    return os.popen(f"ping -c 1 {ip}").read()

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
