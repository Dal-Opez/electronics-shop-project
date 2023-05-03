import pytest
from src.item import Item
from src.phone import Phone

def test_phone_repr():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"

def test_phone_add():
    item = Item("Пылесос", 20000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1 + item == 25

def test_setter_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone1.number_of_sim = 5
    assert phone1.number_of_sim == 5
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0