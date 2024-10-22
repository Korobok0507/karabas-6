# Определяем классы родителя

# Животное
class Animal:
    def __init__(self, name):
        self.name = name  # Индивидуальное название животного
        self.alive = True  # Живое
        self.fed = False   # Голодное

# Растение
class Plant:
    def __init__(self, name):
        self.name = name  # Индивидуальное название растения
        self.edible = False  # Съедобность

# Определяем классы наследников

# Млекопитающее
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} попытался съесть {food.name}")
            self.alive = False

# Хищник
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} попытался съесть {food.name}")
            self.alive = False

# Цветок
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)  # Инициализация родительского класса

# Фрукты
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукты съедобные

# Создаем объекты классов
a1 = Predator('Позорный Волк')
a2 = Mammal('Кракозябер')
p1 = Flower('Кактус')
p2 = Fruit('Зизифус')

# Проверка состояния объектов
print(a1.name)
print(a2.name)
print(p1.name)
print(p2.name)

print(a1.alive)  # True (живой)
print(a2.alive)  # True (живой)
print(a1.fed)    # False (голодный)
print(a2.fed)    # False (голодный)

# Выполняем действия
a1.eat(p1)  # Хищник пытается съесть цветок
a2.eat(p2)  # Млекопитающее ест фрукт

# Проверка состояния объектов после действий
print(a1.alive)  # False (погиб)
print(a1.fed)  # False (голодный)
print(a2.alive)  # True (живой)
print(a2.fed)    # True (насытился)