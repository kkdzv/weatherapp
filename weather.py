from user_city import get_user_city
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import CantGetCity, ApiServiceError


def main():
    try:
        user_city = get_user_city()
    except CantGetCity:
        print("Не удалось получить данные о городе")
        exit(1)
    try:
        weather = get_weather(user_city)
    except ApiServiceError:
        print(f"Не удалось получить погоду по id города {user_city}")
        exit(1)
    print(format_weather(weather))


if __name__ == '__main__':
    main()
