from dataclasses import dataclass


@dataclass
class Coordinate:
    longitude: float
    latitude: float


def get_coordinates() -> Coordinate:
    return Coordinate(longitude=48, latitude=44)


if __name__ == '__main__':
    print(get_coordinates())
