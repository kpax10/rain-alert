import requests
import constants


def telegram_bot_sendtext(bot_message):
    bot_token = constants.TELEGRAM_BOT_TOKEN
    bot_chat_id = constants.TELEGRAM_BOT_ID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


api_key = constants.OWM_API_KEY
api_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
MY_LAT = 33.745472
MY_LONG = -117.867653

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': api_key,
    'cnt': 4,
}

response = requests.get(url=api_endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    weather_code = hour_data['weather'][0]['id']
    if weather_code < 700:
        will_rain = True
if will_rain:
    telegram_bot_sendtext("It's going to rain today.  Remember to bring an umbrella!")
