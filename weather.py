from gps_coordinates import get_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import CantGetCoordinates, ApiServiceError

USER_CITY = 'Voronezh'


def main():
    try:
        coordinates = get_coordinates(USER_CITY)
    except CantGetCoordinates:
        print("Не удалось получить GPS координаты")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print(f"Не удалось получить погоду по координатам {coordinates}")
        exit(1)
    print(format_weather(weather))


if __name__ == '__main__':
    main()
