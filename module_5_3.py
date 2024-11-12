class House:
    def __init__(self, name, number_of_house):
        self.name = name
        self.number_of_house = number_of_house

    def go_to(self, new_flor):
        n_f = int(new_flor)
        for i in range(1, n_f + 1):
            if n_f <= 1 or n_f >= self.number_of_house:
                print("Такого этажа не существует")
                break
            else:
                print(i)

    def __len__(self): #возвращает кол-во этажей здания
        return self.number_of_house

    def __str__(self): #возвращает строку: "Название: <название>, кол-во этажей: <этажи>"
        return f'Название: {self.name}, кол-во этажей: {self.number_of_house}'

    def __eq__(self, other):
       return self.number_of_house == other.number_of_house

    def __lt__(self, other):
        return self.number_of_house < other.number_of_house

    def __le__(self, other):
        return self.number_of_house <= other.number_of_house

    def __gt__(self, other):
        return self.number_of_house > other.number_of_house

    def __ge__(self, other):
        return self.number_of_house >= other.number_of_house

    def __ne__(self, other):
        return self.number_of_house != other.number_of_house

    def __add__(self, value):
        self.number_of_house = self.number_of_house + value
        return self

    def __radd__(self, value):
        self.number_of_house = value + self.number_of_house
        return self

    def __iadd__(self, value):
        self.number_of_house += value
        return self

h1 = House("Дом", 5)
h2 = House("Небоскреб", 38)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 33 # __add__
print(h1)
print(h1 == h2) # __eq__

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

