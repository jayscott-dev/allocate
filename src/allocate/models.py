from __future__ import annotations
from dataclasses import dataclass
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
