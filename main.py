import requests
# import json
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

BASE_URL = 'enter base url'
API_KEY = 'enter api key'

parameters = {
    'lat': # enter latitude,
    'lon': # enter longitude,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily',
}

response = requests.get(BASE_URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
twelve_hour_weather = weather_data['hourly'][0:12:]
twelve_hour_weather_id_codes = [
    twelve_hour_weather[hour_data_index]['weather'][0]['id']
    for hour_data_index
    in range(len(twelve_hour_weather))
    if twelve_hour_weather[hour_data_index]['weather'][0]['id'] < 700
]
# print(twelve_hour_weather_id_codes)

# if len(twelve_hour_weather_id_codes) > 0:
#     print('Bring an umbrella.')
# else:
#     print('You\'re good to go')

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
ACCOUNT_SID = 'enter account sid'
AUTH_TOKEN = 'enter auth token'
# client = Client(ACCOUNT_SID, AUTH_TOKEN)
#
# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+15017122661',
#                      to='+15558675310'
#                  )
#
# print(message.sid)

if len(twelve_hour_weather_id_codes) > 0:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body='It\'s going to rain today, make sure you bring an ☔ with you wherever you go!',
        from_='enter phone number',
        to='enter phone number'
    )

    # print(message.sid)
    print(message.status)
else:
    print('You\'re good to go')
