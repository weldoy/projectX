import requests
import datetime
import sys

# import os
# import json

try:
    print('\nCurrent Bitcoin rate')
    while True:
        request = requests.get(url='https://blockchain.info/ticker')
        if request.status_code == 200:
            now = datetime.datetime.now()
            response = request.json()
            currency = response["USD"]["sell"]
            sys.stdout.write(f'\r{now.strftime("%D - %H:%M:%S")} : {currency}')
            sys.stdout.flush()


except requests.exceptions.ConnectionError:
    print('Check your connection :(')
