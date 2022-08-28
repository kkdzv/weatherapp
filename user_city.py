from dataclasses import dataclass


@dataclass
class City:
    city_id: int


def get_user_city() -> City:
    return City(city_id=524901)


if __name__ == '__main__':
    print(get_user_city())
