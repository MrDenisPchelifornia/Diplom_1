import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

def test_database_available_buns():
    db = Database()
    buns = db.available_buns()
    assert len(buns) == 3

def test_database_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6