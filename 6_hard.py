# Импорт математической библиотеки
import math

# Создание родительского класса фигур
class Figure:
    # Количество сторон по умолчанию (0)
    sides_count = 0

    # Назначение атрибутов (цвет и список сторон) + атрибут заполнености фигуры
    def __init__(self, color=None, *sides):
        self.__sides = []
        self.__color = color
        self.filled = False

        # Назначение цвета, введенного пользователем, если цвет отсутствует
        if self.__color is None:
            self.set_color()

        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count  # Инициализируем стороны по умолчанию
        else:
            self.set_sides(*sides)

    def _is_valid_color(self, r, g, b):
        # Проверяем, находятся ли значения в допустимом диапазоне
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    # Запрос, ввод цвета, проверка корректности ввода
    def set_color(self):
        try:
            r, g, b = map(int, input("Введите значение цвета фигуры r, g, b через запятую: ").split(','))
            if self._is_valid_color(r, g, b):
                self.__color = (r, g, b)
            else:
                print("Введите корректные значения цвета")
                self.set_color()  # Запрашиваем повторный ввод
        except ValueError:
            print("Некорректный ввод. Убедитесь, что вы вводите целые числа.")
            self.set_color()  # Запрашиваем повторный ввод

    # Создание списка r, g, b
    def get_color(self):
        return list(self.__color)

    # Проверка корректности передачи сторон
    def _is_valid_sides(self, *new_sides):
        return all(isinstance(side, (int, float)) and side >= 0 for side in new_sides) and len(
            new_sides) == self.sides_count

    # Устанавливаем длины сторон, если они корректны
    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    # Формирование списка сторон
    def get_sides(self):
        return list(self.__sides)


    # Запрос положительного числа при вводе метрических значений
    def input_positive_number(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                if value >= 0:
                    return value
                else:
                    print("Значение должно быть неотрицательным. Попробуйте снова.")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")

# Дочерний класс круга
class Circle(Figure):
    sides_count = 1 # Назначение количества сторон (в данном случае имеется ввиду радиус)

    def __init__(self, color=None, *sides):
        # Запрашиваем радиус у пользователя
        self.__radius = self.input_positive_number("Введите радиус круга: ")

        # Устанавливаем цвет
        super().__init__(color, self.__radius)  # Передаем радиус в родительский класс
        self.__sides = [self.__radius]  # Сторона - это радиус

    def get_square(self):
        # Вычисляет и возвращает площадь круга.
        return math.pi * (self.__radius ** 2)

    def get_circumference(self):
    # Вычисляет и возвращает длину окружности.
        return 2 * math.pi * self.__radius

    def get_radius(self):
        # Возвращает радиус круга.
        return self.__radius

# Дочерний класс треугольника
class Triangle(Figure):
    sides_count = 3  # Назначение количества сторон

    def __init__(self, color=None, *sides):
        # Сначала запрашиваем размеры сторон
        if len(sides) == 3 and self._is_valid_sides(*sides):
            self.set_sides(*sides)
        else:
            a = self.input_positive_number("Введите размер стороны 'a' треугольника: ")
            b = self.input_positive_number("Введите размер стороны 'b' треугольника: ")
            c = self.input_positive_number("Введите размер стороны 'c' треугольника: ")
            if a + b > c and a + c > b and b + c > a:  # Проверка на возможность построения треугольника
                self.set_sides(a, b, c)
            else:
                print("Невозможно создать треугольник с такими сторонами.")
                return

        super().__init__(color, *self.get_sides())  # Передаем стороны в родительский класс

    # Вычисляем площадь треугольника
    def get_square(self):
        a, b, c = self.get_sides()  # Используем метод get_sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


# Дочерний класс куба
class Cube(Figure):
    sides_count = 1  # У куба только одно значение для ребра

    def __init__(self, color=None, *sides):
        # Сначала запрашиваем размер ребра, проверяем корректность ввода
        if len(sides) == 1 and self._is_valid_sides(*sides):
            side_length = sides[0]
        else:
            side_length = self.input_positive_number("Введите размер ребра куба: ")

        super().__init__(color, side_length)  # Передаем размер ребра в родительский класс
        self.__sides = [side_length]  # Храним только одно значение для ребра

    def get_volume(self):
        return self.get_sides()[0] ** 3  # Используем метод get_sides для получения длины ребра


# Запуск программы
if __name__ == "__main__":
    circle = Circle()
    triangle = Triangle()
    cube = Cube()

    print(f"Площадь круга: {circle.get_square()}")
    print(f"Длина окружности: {circle.get_circumference()}")
    print(f"Цвет круга (RGB): {circle.get_color()}")


    print(f"Площадь треугольника: {triangle.get_square()}")
    print(f"Цвет треугольника (RGB): {triangle.get_color()}")


    print(f"Объем куба: {cube.get_volume()}")
    print(f"Цвет куба (RGB): {cube.get_color()}")