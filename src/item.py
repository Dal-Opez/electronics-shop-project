import csv
import os

BASE_PATH = os.path.abspath("src")


# FILE_NAME = "items_correct.csv"
FILE_NAME = "i_am_not_exist.txt"
# FILE_NAME = "items_structure_error.csv"
FILE_PATH = os.path.join(BASE_PATH, FILE_NAME)  # Полноценный путь к файлу
class InstantiateCSVError(Exception):

    def __str__(self):
        print(f'InstantiateCSVError: Файл "{FILE_NAME}" поврежден.')

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        # return f"{self.name}"
        return self.name

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) <= 10:
            self.__name = name

    @staticmethod
    def string_to_number(number):
        return int(float(number))


    @classmethod
    def instantiate_from_csv(cls):
        # with open("src/items.csv", "r", encoding='windows-1251') as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     for row in reader:
        #         cls(row["name"], row["price"], row["quantity"])
        try:
            with open(FILE_PATH, "r", encoding="windows-1251") as csv_file:
                reader = csv.DictReader(csv_file)
                Item.all.clear()
                correct_columns = ["name", "price", "quantity"]
                if reader.fieldnames == correct_columns:
                    for item in reader:
                        cls(item['name'], item['price'], item['quantity'])
                else:
                    raise InstantiateCSVError
        except InstantiateCSVError:
            print(f'InstantiateCSVError: Файл "{FILE_NAME}" поврежден.')
            # raise InstantiateCSVError

        except FileNotFoundError:
            print(f'FileNotFoundError: Файл "{FILE_NAME}" не найден.')
            # raise FileNotFoundError(f'FileNotFoundError: Файл "{FILE_NAME}" не найден.')



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
