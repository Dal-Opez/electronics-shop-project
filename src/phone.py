from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(self, other.__class__):
            return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self.__number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, number):
        if number > 0 and not isinstance(number, float):
            self.__number_of_sim = number
        else:
            raise ValueError
