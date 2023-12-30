"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item_fixture():
    return Item("test_1", 15.5, 2)




def test__item_init(item_fixture):
    """
    Тест параметров класса.
    """
    assert item_fixture.name == "test_1"
    assert item_fixture.price == 15.5
    assert item_fixture.quantity == 2


def test__calculate_total_price(item_fixture):
    """
    Тест на общую стоимость товара.
    """
    assert item_fixture.calculate_total_price() == 31.0


def test__apply_discount(item_fixture):
    """
    Тест скидки товара.
    """
    item_fixture.pay_rate = 0.5
    item_fixture.apply_discount()
    assert item_fixture.price == 7.75

def test_name_property():
    """Переименование"""
    item = Item("СуперСмартфон", 1000, 2)
    assert item.name == 'СуперСмартфон'

def test_instantiate_from_csv():
    """Достаем из csv объекты класса"""
    Item.instantiate_from_csv('src/items.csv')

    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[2].price == 10
    assert Item.all[3].quantity == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

