import requests
import json
from termcolor import colored

banner = r"""

                                         .--.                .   .
                                         |   )               |  /
                                         |--'   .  .  .  .   |-'
                                         |  \   |  |  |  |   |  \
                                         '   `  `--|  `--`-  '   `
                                                   ;
                                                `-'

"""

banner = colored(banner, 'cyan', attrs=['dark', 'bold'])
print(banner)  # just a banner


# it will search rate according to date
date = input("Enter date in format 'yyyy-mm-dd' :")

convert_from = input("Convert From currency :").upper()
convert_to = input("Convert To currency :").upper()

# How much You want to convert
amount = float(input(f"How much {convert_from} to convert :"))

url = 'https://api.exchangeratesapi.io'  # base url
convert_url = url + '/' + date + '?base=' + \
    convert_from + "&symbols=" + convert_to  # modified url

res = requests.get(convert_url)

if res.ok is False:
    print(f"\nError {res.status_code}")
    print(res.json()['error'])

else:
    data = res.json()
    result = data['rates'][convert_to]
    print(f"\n{amount} {convert_from} into {convert_to} is {result}")
