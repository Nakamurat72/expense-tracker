import sqlite3
from expense_tracker.models import Expense

DB_PATH = "expenses.db"

def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)

def init_db() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL,
                spent_at TEXT NOT NULL
            )
        """)
def add_expense(expense: Expense) -> int:
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO expenses (amount,category,description,spent_at) VALUES (?, ?, ?, ?)",
            (str(expense.amount), expense.category, expense.description, expense.spent_at.isoformat()),
        )
        return cursor.lastrowid