
import sqlite3
import hashlib
import secrets
import hmac

DB_NAME = "users.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE COLLATE NOCASE,
            username TEXT NOT NULL UNIQUE COLLATE NOCASE,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt),
        200000
    ).hex()

    return password_hash, salt


def register_user(full_name, email, username, password):
    conn = sqlite3.connect(DB_NAME)

    try:
        password_hash, salt = hash_password(password)

        conn.execute("""
            INSERT INTO users
            (full_name, email, username, password_hash, salt)
            VALUES (?, ?, ?, ?, ?)
        """, (
            full_name,
            email,
            username,
            password_hash,
            salt
        ))

        conn.commit()
        return True, "Registration successful!"

    except sqlite3.IntegrityError:
        return False, "Username or email already exists."

    finally:
        conn.close()


def login_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    user = conn.execute("""
        SELECT * FROM users
        WHERE username = ? COLLATE NOCASE
    """, (username,)).fetchone()

    conn.close()

    if user is None:
        return None

    stored_hash, salt = user["password_hash"], user["salt"]

    entered_hash, _ = hash_password(password, salt)

    if hmac.compare_digest(stored_hash, entered_hash):
        return {
            "id": user["id"],
            "full_name": user["full_name"],
            "email": user["email"],
            "username": user["username"]
        }

    return None
