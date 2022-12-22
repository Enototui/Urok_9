import requests
from bs4 import BeautifulSoup as bs
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime
import pandas as pd
url = 'https://yandex.by/pogoda/details/10-day-weather?lat=52.79291916&lon=27.54374695&via=mf#22'
response = requests.get(url).text
soup = bs(response, 'html.parser')
weather = soup.find('strong', class_="forecast-details__day-number")
print('Погода в Солигорске:', weather.text, '°C')
