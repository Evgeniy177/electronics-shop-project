import csv
from pathlib import Path

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        self.__name = name  # Приватный атрибут name
        self.price = price
        self.quantity = quantity
        self.all.append(self)  # Добавляем созданный объект в список all

