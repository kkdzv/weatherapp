import json
import ssl
import urllib
from dataclasses import dataclass
from urllib.error import URLError
import urllib.request
from requests import JSONDecodeError
import config
from exceptions import CantGetUserCity


@dataclass
class Coordinate:
    longitude: float
    latitude: float


def get_coordinates(city: str) -> Coordinate:
    coordinates_response = _get_coordinates_response(city)
    coords = _parse_coordinates_response(coordinates_response)
    return coords


def _get_coordinates_response(city) -> str:
    ssl.create_default_https_context = ssl.create_default_context()
    url = config.OPENWEATHER_URL_COORDS.format(city_req=city)
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise CantGetUserCity


def _parse_coordinates_response(openweather_response: str) -> Coordinate:
    try:
        openweather_dict = json.loads(openweather_response)
    except JSONDecodeError:
        raise JSONDecodeError
    return Coordinate(
        longitude=_parse_coords_longitude(openweather_dict),
        latitude=_parse_coords_latitude(openweather_dict)
    )


def _parse_coords_longitude(openweather_dict: dict) -> float:
    try:
        return openweather_dict[0]['lon']
    except (IndexError, KeyError):
        raise CantGetUserCity('Нет данных о городе')


def _parse_coords_latitude(openweather_dict: dict) -> float:
    try:
        return openweather_dict[0]['lat']
    except (IndexError, KeyError):
        raise CantGetUserCity('Нет данных о городе')


if __name__ == '__main__':
    USER_CITY = "Armavir"
    print(get_coordinates(USER_CITY))
