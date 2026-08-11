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
