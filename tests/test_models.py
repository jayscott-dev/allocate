from src.allocate.models import Budget, Category

def test_category():
    data = {
        "name": "test category",
        "target": 1000,
        "period": "yearly",
    }

    category = Category.from_dict(data)

    assert category.name == "test category"
    assert category.target == 1000
    assert category.period == "yearly"
    assert not category.subscription

def test_budget():
    data = {
        "name": "test budget",
        "selected": True,
        "categories": [{
            "name": "test category",
            "target": 1000,
            "period": "yearly",
        }] 
    }

    budget = Budget.from_dict(data)

    assert budget.name == "test budget"
    assert budget.selected
    assert budget.categories[0].name == "test category"
    