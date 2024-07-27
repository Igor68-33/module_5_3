# Различие атрибутов класса и экземпляра

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(f"Этаж: {i + 1}")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + int(other)
            return self

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + int(other)
            return self

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + int(other)
            return self

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# Вывод на консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории
