from allocate.models import Budget
from pathlib import Path
import json

def allocate_budget(total: int, budgets_file: Path):
    with budgets_file.open("r") as f:
        raw_data = json.loads(f.read())

    budgets = [Budget.from_dict(budget) for budget in raw_data.get("budgets", [])]

    for b in budgets:
        if b.selected:
            b.display_category_table(total)
    