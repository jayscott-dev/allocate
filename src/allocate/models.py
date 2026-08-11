from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass
class Category:
    name: str
    target: int
    period: str
    subscription: bool

    @classmethod
    def from_dict(cls, category: dict) -> Category:
        return cls (
            name = category["name"],
            target = category["target"],
            period = category["period"],
            subscription = category.get("subscription", False),
        )
    
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
