# Web Security CTF Lab

A deliberately vulnerable Flask-based web application designed as a small **Capture The Flag (CTF) and web application security practice lab**.

The project contains multiple intentionally insecure web functionality examples that can be used for learning about common web security vulnerabilities in a controlled local environment.

> **Warning:** This application is intentionally vulnerable. Run it only on a local machine or an isolated lab environment. Do not deploy it to a public or production server.

## Vulnerabilities Demonstrated

The application contains intentionally vulnerable implementations of:

- SQL Injection
- Cookie Manipulation
- Hidden Routes
- Cross-Site Scripting (XSS)
- Unrestricted File Upload
- Server-Side Request Forgery (SSRF)
- Insecure Direct Object Reference (IDOR)
- Command Injection
- Source-Code / HTML Inspection challenges

Each vulnerability is associated with a CTF-style flag or challenge objective.

## Project Structure

```text
CTF-lab/
│
├── app.py
├── requirement.txt
│
└── templates/
    ├── index.html
    ├── login.html
    └── comments.html
```

## Technologies Used

- Python
- Flask
- SQLite
- Requests
- PyJWT
- Gunicorn
- HTML

## Requirements

Install the dependencies using:

```bash
pip install -r requirement.txt
```

## Running the Lab

Start the Flask application:

```bash
python app.py
```

The application listens on:

```text
http://127.0.0.1:5000
```

Open the URL in a browser.

## Database

The application automatically creates a SQLite database:

```text
users.db
```

The database contains a sample administrative account for the laboratory environment.

The application initializes the database when `app.py` starts.

## CTF Challenges

### 1. Source Inspection

The homepage contains a hidden challenge that can be discovered through HTML/source inspection.

### 2. SQL Injection

The login endpoint constructs an SQL query directly from user-controlled input.

This demonstrates the risks of:

- String-built SQL queries
- Unsanitized input
- Missing parameterized statements

### 3. Cookie Manipulation

The application uses a client-side `role` cookie to determine access to the dashboard.

This demonstrates why authorization decisions should not rely on untrusted client-controlled values.

### 4. Hidden Directory / Route

A non-linked administrative route is included to demonstrate discovery of hidden application endpoints.

### 5. Cross-Site Scripting

The comment functionality intentionally renders submitted content without escaping it.

This demonstrates the risk of:

- Stored XSS
- Unsafe HTML rendering
- Unsanitized user input

### 6. File Upload

The application accepts uploaded files and stores them under the configured upload directory.

This demonstrates risks associated with unrestricted file uploads.

### 7. SSRF

The `/fetch` endpoint retrieves a URL supplied by the user.

This demonstrates the basic concept of Server-Side Request Forgery, where a server is tricked into making requests on behalf of a user.

### 8. IDOR

The `/profile` endpoint accesses user records based on a supplied identifier.

This demonstrates insecure access control when object identifiers are accepted without proper authorization checks.

### 9. Command Injection

The `/ping` endpoint passes user-controlled input to a system command.

This demonstrates why untrusted data should never be directly inserted into shell commands.

## Learning Objectives

This project is intended to help students understand:

- Web application attack surfaces
- Common OWASP-style vulnerabilities
- Input validation
- Authentication and authorization
- Secure database queries
- Output encoding
- Secure file handling
- Server-side request security
- Access control
- OS command security

## Security Concepts

The lab demonstrates why secure applications should use techniques such as:

```text
Parameterized SQL Queries
        ↓
Input Validation
        ↓
Output Encoding
        ↓
Secure Authentication
        ↓
Server-Side Authorization
        ↓
Safe File Handling
        ↓
SSRF Protection
        ↓
Safe Process Execution
```

## Intended Environment

This project is intended for:

- Cybersecurity labs
- CTF practice
- Web security demonstrations
- Secure coding education
- Vulnerability research in isolated environments

## Important Security Notice

The vulnerabilities in this project are intentional and are included for educational purposes.

Do not expose this application to:

- The public internet
- Production networks
- Untrusted users
- Systems containing sensitive information

Use an isolated local or virtual-machine environment for testing.

## Future Enhancements

Possible additions include:

- More CTF challenges
- User registration
- Authentication challenges
- JWT security challenges
- CSRF challenges
- Path traversal
- Command execution challenges
- API security challenges
- Authentication bypass challenges
- Docker-based deployment
- Automated flag validation
- Challenge scoring
- CTF scoreboard

## Academic / Security Lab Project

This project was developed as a cybersecurity learning environment for understanding common web application vulnerabilities through hands-on CTF-style challenges.
