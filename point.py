import math
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    z: int

    def x_norm(self):
        return abs(self.x)

    def y_norm(self):
        return abs(self.y)

    def z_norm(self):
        return abs(self.z)

    def l1_norm(self):
        return sum([self.x_norm(), self.y_norm(), self.z_norm()])

    def l2_norm(self):
        return math.hypot(self.x_norm(), self.y_norm(), self.z_norm())

    def cyclic_transpose(self):
        self.x, self.y, self.z = self.y, self.z, self.x


if __name__ == "__main__":
    point1 = Point(1, 2, 3)
    point2 = Point(2, 3, 4)

    print(point1)
    print(point2)

    print(point1.l1_norm())
    print(point1.l2_norm())
    
    point1.cyclic_transpose()
    print(point1)
