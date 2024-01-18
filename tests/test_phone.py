from src.phone import Phone


def test_phone_init():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_phone_add():
        phone = Phone("iPhone 14", 120_000, 5, 2)
        phone1 = Phone("Samsung A 54", 80_000, 10, 1)
        assert phone.quantity + phone1.quantity == 15



def test_phone_str():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone) == "iPhone 14"


def test_phone_repr():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"