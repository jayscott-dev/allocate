from __future__ import annotations
from dataclasses import dataclass
from rich.console import Console
from rich.table import Table
import math

@dataclass
class Category:
    name: str
    target: int
    period: str
    subscription: bool

    @classmethod
    def from_dict(cls, category: dict) -> Category:
        target = category["target"]
        period = category["period"]

        return cls (
            name = category["name"],
            target = target,
            period = period,
            subscription = category.get("subscription", False),
        )

    @property
    def allocation_amount(self) -> int:
        if self.period == "yearly":
            pay_periods = 24
        else:
            pay_periods = 2

        return math.ceil(self.target / pay_periods)
    
@dataclass
class Budget:
    name: str
    categories: list[Category]
    selected: bool

    @classmethod
    def from_dict(cls, budget: dict) -> Budget:
        return cls (
            name = budget["name"],
            selected = budget.get("selected", False),
            categories = [Category.from_dict(category) for category in budget["categories"]]
        )

    def display_category_table(self, income_amount: int):
        console = Console()
        table = Table(title = f"{self.name} Allocations")
        allocated_amount = 0

        table.add_column("Amount", justify = "right", style = "green")
        table.add_column("Category Name", style = "magenta", no_wrap = True)
        table.add_column("Target Amount", justify = "right", style = "blue")
        table.add_column("Period")
        table.add_column("Subscription")

        for category in sorted(self.categories, key = lambda category: category.allocation_amount, reverse = True):
            allocated_amount = allocated_amount + category.allocation_amount
            table.add_row(
                str(category.allocation_amount),
                category.name,
                str(category.target),
                category.period.capitalize(),
                f"{"Yes" if category.subscription else "No"}",
            )

        print()
        console.print(table)

        summary = Table(title = "Summary")
        overflow_amount = income_amount - allocated_amount

        summary.add_column("Total Allocated", justify = "right", style = "green")
        summary.add_column("Overflow", justify = "right", style = f"{"blue" if overflow_amount >= 0 else "red"}")

        summary.add_row(
            str(allocated_amount),
            str(overflow_amount),
        )

        console.print(summary)
        print()
