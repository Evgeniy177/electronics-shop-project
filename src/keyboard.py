from src.item import Item


class Mixin_Lang:
    """
    Миксин для изменения языка клавиатуры.
    """





    def change_lang(self):
        """
        Метод для изменения языка клавиатуры.
        """
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"



class Keyboard(Mixin_Lang, Item):
    """
    Класс для представления товара "клавиатура" с возможностью изменения языка.
    """
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.language = 'EN'