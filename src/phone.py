from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, count_of_sim: int):
        super().__init__(name, price, quantity,)
        self.__count_of_sim = count_of_sim

    def __add__(self, other):
        if isinstance(other, self.__class__) or issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        else:
            raise ValueError("Складывать можно только экземпляры класса")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    @property
    def number_of_sim(self):
        """Геттер sim- карт"""
        return self.__count_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num):
        """Сеттер числа sim- карт"""
        if float(num) == int(num) and int(num) > 0:
            self.__count_of_sim = num
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")