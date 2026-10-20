from dataclasses import dataclass
from datetime import date
from decimal import Decimal

CATEGORIES = {"food", "transport", "rent", "bills", "entertainment", "other"}

@dataclass
class Expense:
    amount: Decimal
    category: str
    description: str
    spent_at: date

    def __post_init__(self) -> None:
        if self.amount <= 0:
            raise ValueError("Amount must be positive")
        if not self.description:
            raise ValueError("Description cannot be empty")
        if self.category not in CATEGORIES:
            raise ValueError("Category must be one of {}".format(CATEGORIES))

