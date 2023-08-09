class Car:
    total_cars = 0

    def __init__(self, make, model, year):
        self.__make = None
        self.__make = make
        self.__model = model
        self.__year = year
        Car.total_cars += 1

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def __str__(self):
        return f"Car made by {self.__make}, model is {self.__model}, produced in {self.__year}"

    @classmethod
    def print_count(cls):
        print(cls.total_cars)


car1 = Car('Bayerische Motoren Werke AG', 'M3', 2004)
car2 = Car('Bayerische Motoren Werke AG', 'M5', 2014)
car3 = Car('Bayerische Motoren Werke AG', 'M8', 2023)
print(car3)
Car.print_count()