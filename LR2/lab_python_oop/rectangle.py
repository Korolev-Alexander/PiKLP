from .figure import GeometricFigure
from .color import FigureColor

class Rectangle(GeometricFigure):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height

    @staticmethod
    def figure_type():
        return "Прямоугольник"

    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {}. Площадь: {}".format(
            self.figure_type(), self.color.color, self.width, self.height, self.area()
        )
