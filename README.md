# Custom URL Shortener Backend

A lightweight, robust URL shortening backend built with Python, Flask, and SQLite3. This application takes long URLs, secures them using SHA-256 hash with an added salt, converts the output to Base-62, and manages collisions dynamically.

## Features
* **Base-62 Encoding:** Translates large hash integers into compact, URL-safe strings using `[0-9][a-z][A-Z]`.
* **Collision Resolution:** If a short hash already exists, the database layer automatically expands the hash slice length until a unique primary key is secured.
* **Persistent Storage:** Uses SQLite3 with built-in integrity checks to handle duplicate URL submissions efficiently.

## Tech Stack
* **Backend Framework:** Flask (Python)
* **Database:** SQLite3
* **Hashing/Security:** `hashlib` (SHA-256), `os.urandom` (Salting)

## How to Run Locally
```bash
git clone <YOUR_REPO_URL>
cd <YOUR_REPO_NAME>
