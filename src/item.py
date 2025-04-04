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

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> None:
        """
        Инициализирует экземпляры класса Item данными из CSV-файла.
        """
        current_file_path = Path(__file__)
        file_path = current_file_path.parent.parent / 'src/items.csv'

        with open(file_path, 'r', encoding='windows-1251') as file:
            cls.all.clear()
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Преобразует строку в число.
        """
        return int(float(value))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return self.__name

Item.instantiate_from_csv('src/items.csv')

