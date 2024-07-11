import pytest
from praktikum.bun import Bun

def test_bun_get_name():
    bun = Bun("test_bun", 50)
    assert bun.get_name() == "test_bun"

def test_bun_get_price():
    bun = Bun("test_bun", 50)
    assert bun.get_price() == 50