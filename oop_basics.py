"""Examples of inheritance and operator overloading."""
from dataclasses import dataclass
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


@dataclass
class Rectangle(Shape):
    width: float
    height: float

    def area(self):
        return self.width * self.height


@dataclass
class Circle(Shape):
    radius: float

    def area(self):
        from math import pi
        return pi * self.radius ** 2


@dataclass(frozen=True)
class Vector:
    x: float
    y: float

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    for shape in [Rectangle(3, 4), Circle(2)]:
        print(shape.area())
    print(Vector(1, 2) + Vector(3, 4))
