"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def class_example_fixture_1():
    return Item("Чайник", 5000, 10)

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert Item.all[0].name == "Смартфон"
    assert Item.all[0].price == "100"
    assert Item.all[0].quantity == "1"

def test_calculate_total_price():
    # pass
    assert Item("Чайник", 5000, 10).calculate_total_price() == 50000
    assert Item("Миксер", 3000, 3).calculate_total_price() == 9000
    assert Item("Пылесос", 15000, 3).calculate_total_price() == 45000

def test_name():
    item = Item("Чайник", 5000, 10)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = 'СуперСмартфон'
    assert item.name == 'Смартфон'

def test_string_to_number():
    assert Item.string_to_number('5') == 5

def test_apply_discount():
    item = Item("Чайник", 5000, 10)
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 2500

def test_item_repr():
    item1 = Item("Микроволновка", 20000, 20)
    assert repr(item1) == "Item('Микроволновка', 20000, 20)"

def test_str():
    item2 = Item("Чайник", 4000, 20)
    assert str(item2) == "Чайник"

def test_item_add():
    item3 = Item("Пылесос", 20000, 20)
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert item3 + phone == 25