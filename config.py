
OPEN_WEATHER_API_KEY ='26c2f492e61ba4c72612cab2df57ca1f'
OPENWEATHER_URL_WEATHER = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "id={city_id}&"
    "appid=" + OPEN_WEATHER_API_KEY + "&lang=ru&"
    "units=metric"
)
OPENWEATHER_URL_COORDS = (
            'http://api.openweathermap.org/geo/1.0/direct?q={city_req},&limit=1&zip=E14&appid=' + OPEN_WEATHER_API_KEY)