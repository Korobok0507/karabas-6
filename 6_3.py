class Chebur:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Мы строили, строили...'  # Речь Чебурашки

    def run(self, dx):
        self.x_distance += dx  # Увеличиваем пройденный путь


class Gena:
    def __init__(self):
        self.y_distance = 0  # Глубина
        self.sound = 'Пусть бегут неуклюже пешеходы по лужам...'  # Песенка Крокодила Гены

    def float(self, dy):
        self.y_distance += dy  # Увеличиваем глубину


class Cheburgen(Chebur, Gena):
    def __init__(self):
        Chebur.__init__(self)  # Инициализация родительского класса Chebur
        Gena.__init__(self)  # Инициализация родительского класса Gena

    def move(self, dx, dy):
        super().run(dx)  # Вызываем метод run из класса Chebur
        super().float(dy)  # Вызываем метод float из класса Gena

    def get_pos(self):
        return (self.x_distance, self.y_distance)  # Возвращаем текущее положение

    def voice(self):
        print(self.sound)  # Печатаем звук, который издаёт Чебурген
        # (наследуется из второго родительского класса по порядку обращения)


# Пример работы программы
cg1 = Cheburgen()

print(cg1.get_pos())
cg1.move(10, 15)
print(cg1.get_pos())
cg1.move(-5, 20)
print(cg1.get_pos())

cg1.voice()