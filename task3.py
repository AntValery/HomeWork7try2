"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П С попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""

class Worker:
    name, surname, position = "", "", ""
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def __str__(self):
        return self.name + " " + self.surname + ", доход: " + str(self._income.get("wage")) + ", премия: " + str(self._income.get("bonus"))

    def __print__(self):
         pass

    def __format__(self, format_spec):
        pass

class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname + ", " + self.position

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")

p = Position("Иван","Иванов","Главный специалист", 50000, 30000)
print(p.get_full_name())
print(p.get_total_income())
print(str(p))
print(p)
