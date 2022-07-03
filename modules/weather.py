import requests
import datetime as dt

def weather_report(city, lang):
    param = {
        'q': city,
        'lang': lang,
        'units': 'metric',
        'appid': '',
    }

    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=param)
    
    if response:
        json = response.json()
        weather_desc = json['weather'][0]['description']                                                            #   Прогноз
        weather_city = json['name']                                                                                 #   Город
        weather_city_id = json['id']                                                                                #   ID на openweathermap
        weather_country = json['sys']['country']                                                                    #   Страна
        weather_time = dt.datetime.utcfromtimestamp(json['dt'] + json['timezone'])                                  #   Время
        weather_real_temp = json['main']['feels_like']                                                              #   Как ощущается температура
        weather_temp = json['main']['temp']                                                                         #   Температура
        weather_temp_min = json['main']['temp_min']                                                                 #   Минимальная температура
        weather_temp_max = json['main']['temp_max']                                                                 #   Максимальная температура
        weather_pressure = json['main']['pressure']                                                                 #   Давление
        weather_humidity = json['main']['humidity']                                                                 #   Влажность
        weather_sea_level = json['main']['sea_level']                                                               #   Уровень моря
        weather_grnd_level = json['main']['grnd_level']                                                             #   Уровень поверхности
        weather_visibility = json['visibility']                                                                     #   Видимость
        weather_wind_speed = json['wind']['speed']                                                                  #   Скорость ветра
        weather_wind_degreee = json['wind']['deg']                                                                  #   Угол направления ветра
        weather_wind_gust = json['wind']['gust']                                                                    #   Порывы ветра
        weather_cloud_status = json['clouds']['all']                                                                #   Процент облачности
        weather_sunrise = dt.datetime.utcfromtimestamp(json['sys']['sunrise'])                                      #   Время рассвета
        weather_sunset = dt.datetime.utcfromtimestamp(json['sys']['sunset'])                                        #   Время заката
        
        result = list()
        result.append(weather_city)
        result.append(weather_country)
        result.append(weather_time)
        result.append(weather_desc.capitalize())
        result.append(weather_temp)
        result.append(weather_real_temp)
        result.append(weather_wind_speed)
        result.append(weather_pressure)
        result.append(weather_humidity)
        result.append(weather_city_id)

        # result = f'Weather info for {weather_city}, {weather_country}: \n\nTime: {weather_time} \nDescription: {weather_desc.capitalize()} \nTemperature: {weather_temp}°C (Feels like: {weather_real_temp}°C) \nWing speed: {weather_wind_speed} m/s \nPressure: {weather_pressure} Pa \nHumidity: {weather_humidity}%'
    else:
        result = None

    return result
