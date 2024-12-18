import math
from .figure import GeometricFigure
from .color import FigureColor

class Circle(GeometricFigure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * self.radius ** 2

    @staticmethod
    def figure_type():
        return "Круг"

    def __repr__(self):
        return "{} {} цвета радиусом {}. Площадь: {:.2f}".format(
            self.figure_type(), self.color.color, self.radius, self.area()
        )

