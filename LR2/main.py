import sys
import requests
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    N = 28  # Ваш вариант

    rectangle = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")

    print(rectangle)
    print(circle)
    print(square)

    # Пример использования внешнего пакета
    response = requests.get("https://api.github.com")
    print("Статус запроса к GitHub API:", response.status_code)

if __name__ == "__main__":
    main()