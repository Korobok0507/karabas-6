# Создание родительского класса (транспортных средств)
class Vehicle:
    # Атрибут класса с возможными вариантами цвета
    __COLOR_VARIANTS = ['детская неожиданность', 'мокрый асфальт', 'мокрая жаба', 'мокрая курица', 'мокрая вода']

    # Инициализация атрибутов объектов
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    # Создание методов отображения информации о транспортном средстве
    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    # Функция вывода информации
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    # Определение возможности замены цвета по заданному
    # списку с приведением к нижнему регистру для корректного сравнения
    def set_color(self, new_color: str):
        if new_color.lower() in [c.lower() for c in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

# Создание дочернего класса
class Sedan(Vehicle):
    # Атрибут класса (остальное наследуется из родительского)
    __PASSENGERS_LIMIT = 5


# Пример использования
vehicle1 = Sedan('Чебурашка', 'ЗАЗ-965', 'Мокрый Крокодил Гена', 2000)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы) и проверяем, что поменялось
vehicle1.set_color('Кровавая ромашка')
vehicle1.print_info()
vehicle1.set_color('Мокрая Курица')
vehicle1.print_info()
vehicle1.owner = 'Шапокляк'
vehicle1.print_info()