import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent / "employees.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL CHECK(age >= 18),
                department TEXT NOT NULL,
                designation TEXT NOT NULL,
                basic_salary REAL NOT NULL CHECK(basic_salary > 0),
                email TEXT UNIQUE,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)
