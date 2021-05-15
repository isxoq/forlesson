class Person:
    name = ""

    def __init__(self, name) -> None:
        self.name = name
        self.__age = 22

    def getName(self):
        return self.name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


class Employee(Person):

    def __init__(self, name, company) -> None:
        super().__init__(name)
        self.company = company
