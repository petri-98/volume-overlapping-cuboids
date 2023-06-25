from point import Point


class Cuboid:

    def __init__(self, p_min: Point, p_max: Point):
        self.p_min = p_min
        self.p_max = p_max
        if any([self.p_min.x >= self.p_max.x, self.p_min.y >= self.p_max.y, self.p_min.z >= self.p_max.z]):
            raise ValueError("Invalid points to create a cuboid!")

    def __repr__(self) -> str:
        return f"Cuboid: [{self.p_min.x},{self.p_max.x}] x [{self.p_min.y},{self.p_max.y}] x [{self.p_min.z},{self.p_max.z}]"

    def get_x_extension(self):
        return self.p_max.x - self.p_min.x

    def get_y_extension(self):
        return self.p_max.y - self.p_min.y

    def get_z_extension(self):
        return self.p_max.z - self.p_min.z

    def get_volume(self) -> int:
        return self.get_x_extension() * self.get_y_extension() * self.get_z_extension()

    def get_surface_area(self) -> int:
        return 2 * (self.get_x_extension() * self.get_y_extension() + self.get_y_extension() * self.get_z_extension() +
                    self.get_x_extension() * self.get_z_extension())

    def cyclic_transpose_cuboid(self):
        self.p_min.cyclic_transpose()
        self.p_max.cyclic_transpose()
        return self


if __name__ == "__main__":

    p_min = Point(1, 5, 12)
    p_max = Point(7, 15, 16)

    cuboid = Cuboid(p_min=p_min, p_max=p_max)

    print(cuboid)
    print(f"The volume is {cuboid.get_volume()}")
    print(f"The surface area is {cuboid.get_surface_area()}")
    print(f"Transposed cuboid: {cuboid.cyclic_transpose_cuboid()}")
