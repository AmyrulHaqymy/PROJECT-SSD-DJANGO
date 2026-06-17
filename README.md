
# Secure Task Management CRUD Web Application

## 1. Project Description
This is a secure web-based CRUD application developed using the Django framework for the **IKB21503 Secure Software Development** course. The system applies a "Security-by-Design" architecture to mitigate common web application vulnerabilities outlined in the OWASP Top 10 and OWASP ASVS standards. The core application allows users to securely authenticate, manage personal task structures, and logs critical transactional boundaries to prevent privilege escalation.

---

## 2. Security Features Summary
* **OWASP A01:2021 – Broken Access Control Mitigation:** Explicit server-side validation restricts administrative URLs (such as `/audit-log/`) strictly to superusers using robust backend decorators. Unauthorized access attempts automatically trigger an `HTTP 403 Forbidden` response and terminate the request thread.
* **OWASP A03:2021 – Injection Mitigation:** Built entirely using **Django ORM** to execute natively parameterized queries. This ensures that user entries into text inputs are treated strictly as structured literals, completely eliminating SQL Injection (SQLi) vectors.
* **OWASP A05:2021 – Security Misconfiguration Isolation:** Production-sensitive hooks (`SECRET_KEY`, `DEBUG=False`) are fully decoupled from the deployment code logic and isolated inside a local, unindexed `.env` configuration block.
* **OWASP ASVS V3 Session Management:** Enforces automated session invalidation and idle-timeout tokens after exactly **5 minutes (300 seconds)** of continuous user inactivity to prevent terminal abandonment risks.
* **OWASP ASVS V8 Audit Logging:** An automated transactional tracking subsystem monitors database mutations (CRUD Trail), registering User Identity metrics, event actions, and high-precision timestamps for full accountability.

---

## 3. Dependencies
The system relies on the following core baseline dependencies:
* **Python 3.14+** (Core Execution Runtime)
* **Django 6.0.6** (Secure MVC Web Framework)
* **python-dotenv** (Environment Configuration Parser)

---

## 4. Installation Steps

### Step 1: Clone the Repository
Pull down the project files from the remote source control pipeline:
`git clone https://github.com/AmyrulHaqymy/PROJECT-SSD-DJANGO.git`
`cd PROJECT-SSD-DJANGO`

### Step 2: Initialize and Activate Virtual Environment
Isolate execution dependencies locally using Python's virtual environment wrapper:
`python -m venv .venv`

# Activation for Windows (PowerShell):
`.venv\Scripts\activate`

### Step 3: Install Required Dependencies
Pull and install core runtime components from the package repository index:
`pip install django python-dotenv`

### Step 4: Configure Local Environment Parameters
Generate your local configuration file by duplicating the provided secure fallback template:
`cp .env.example .env`

---

## 5. How to Run the App

### Step 1: Navigate to Source Context
Move your terminal execution context into the primary Django workspace directory:
`cd secure-crud-app/src`

### Step 2: Initialize Database Migrations
Sync database tracking tables and compile structural definitions locally:
`python manage.py migrate`

### Step 3: Launch Secure Development Server
Initialize the local web application pipeline:
`python manage.py runserver`

The secure workspace portal will now listen locally at: http://127.0.0.1:8000/

---

## 6. System Testing & Evidence Screenshots

### Security Monitoring Architecture (Audit Log View)
Displays the operational monitoring trail accessible only by authorized administrative users, highlighting comprehensive transaction auditing.

### Access Violation Deflection (HTTP 403 Runtime Proof)
Verification evidence showing the system's defensive layer catching an illegal route violation attempt, securely breaking the thread with a generic 403 restriction log.