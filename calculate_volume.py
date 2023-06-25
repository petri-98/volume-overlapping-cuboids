from collections import defaultdict

from cuboid import Cuboid
from point import Point


def get_area_step(y_line: defaultdict, prev_x: int, x: int) -> int:
    """Auxiliary function to calculate area in the sweep-line algorithm."""
    area = 0
    prev_y = float('-inf')
    active_rectangles = 0

    for y, count in sorted(y_line.items()):
        active_rectangles += count

        if active_rectangles == count:
            prev_y = y

        if active_rectangles == 0:
            area += (y - prev_y) * (x - prev_x)

    return area


def compute_area(cuboids: list[Cuboid]) -> int:
    """Computes the total area of the union of the rectangles (projections of the cuboids on the xy plane) taking into account the overlaps using a sweep-line-based algorithm.

    Args:
        cuboids (list[Cuboid]): List of cuboids.

    Returns:
        int: Total area of the union of the rectangles (taking into account the overlaps).
    """
    events = []

    for cuboid in cuboids:
        events.append([cuboid.p_min.x, 0, cuboid.p_min.y, cuboid.p_max.y])  # Start event
        events.append([cuboid.p_max.x, 1, cuboid.p_min.y, cuboid.p_max.y])  # End event

    events.sort(key=lambda x: (x[0], x[1]))  # Sort events by x-coordinate and event type

    area = 0
    prev_x = float('-inf')
    y_line = defaultdict(int)

    for event in events:
        x, is_end, y1, y2 = event

        if prev_x != float('-inf'):
            area += get_area_step(y_line, prev_x, x)

        if is_end:
            y_line[y1] -= 1
            y_line[y2] += 1

        else:
            y_line[y1] += 1
            y_line[y2] -= 1

        prev_x = x

    return area


def compute_volume(cuboids: list[Cuboid]) -> int:
    """Computes the total volume of the union of the cuboids taking into account the overlaps using a sweep-line-based algorithm.

    Args:
        cuboids (list[Cuboid]): List of cuboids.

    Returns:
        int: Total volume of the union of the cuboids (taking into account the overlaps).
    """
    events = []
    volume = 0

    for cuboid in cuboids:
        events.append([cuboid.p_min.x, 0, cuboid.p_min.y, cuboid.p_max.y, cuboid.p_min.z, cuboid.p_max.z])
        events.append([cuboid.p_max.x, 1, cuboid.p_min.y, cuboid.p_max.y, cuboid.p_min.z, cuboid.p_max.z])

    if events:
        events.sort(key=lambda x: (x[0], x[1]))
        prev_x = events[0][0]

        for event in events[1:]:
            transposed_cuboids = [
                cuboid.cyclic_transpose_cuboid() for cuboid in cuboids
                if prev_x in range(cuboid.p_min.x, cuboid.p_max.x)
            ]
            volume += compute_area(transposed_cuboids) * (event[0] - prev_x)
            prev_x = event[0]
    return volume


if __name__ == "__main__":

    cuboid1 = Cuboid(p_min=Point(1, 1, 1), p_max=Point(2, 2, 2))

    cuboid2 = Cuboid(p_min=Point(1, 1, 1), p_max=Point(3, 3, 3))

    cuboid3 = Cuboid(p_min=Point(3, 3, 3), p_max=Point(4, 4, 4))

    cuboids = [cuboid1, cuboid2, cuboid3]

    print(f"The total volume of the union of the cuboids is {compute_volume(cuboids)}.")
