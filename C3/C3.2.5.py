class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, plane):
        self.plane = plane

    def input_plane(self):
        # try:

        self.plane = int(input("Введите сторону квадрата: "))
        if self.plane <= 0:
            raise NonPositiveDigitException("Wrong value")

        return print(f"Значение {self.plane} успешно записано")

    def show_square_area(self):
        return f'Площадь квадрата: {self.plane ** 2}'


square = Square
square.input_plane(0)
print(square.show_square_area())
