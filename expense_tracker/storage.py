import sqlite3

from unicodedata import category

from expense_tracker.models import Expense
from datetime import date
from decimal import Decimal

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

def list_expenses() -> list[Expense]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, amount, category, description, spent_at FROM expenses ORDER BY spent_at"
        ).fetchall()
    return [
        Expense(
            amount=Decimal(row[1]),
            category=row[2],
            description=row[3],
            spent_at=date.fromisoformat(row[4]),
            id=row[0],
        )
        for row in rows
    ]

