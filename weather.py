from user_city import get_user_city
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import CantGetCoordinates, ApiServiceError


def main():
    try:
        user_city = get_user_city()
    except CantGetCoordinates:
        print("Не удалось получить GPS координаты")
        exit(1)
    try:
        weather = get_weather(user_city)
    except ApiServiceError:
        print(f"Не удалось получить погоду по координатам {user_city}")
        exit(1)
    print(format_weather(weather))


if __name__ == '__main__':
    main()
