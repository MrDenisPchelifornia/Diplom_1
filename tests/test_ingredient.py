import pytest
from praktikum.ingredient import Ingredient

def test_ingredient_get_name():
    ingredient = Ingredient("FILLING", "test_filling", 30)
    assert ingredient.get_name() == "test_filling"

def test_ingredient_get_price():
    ingredient = Ingredient("FILLING", "test_filling", 30)
    assert ingredient.get_price() == 30

def test_ingredient_get_type():
    ingredient = Ingredient("FILLING", "test_filling", 30)
    assert ingredient.get_type() == "FILLING"