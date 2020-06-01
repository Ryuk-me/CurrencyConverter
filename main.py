import requests
from random import choice
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format('Ryuk-Me')
header = colored(header,color='red')
print(header)

url = 'https://icanhazdadjoke.com/search'

user_input = input('Enter Jokes You want to search :')

res = requests.get (url,
    headers={'Accept': 'application/json'},
    params={'term':user_input}
    ).json()

total = res['total_jokes'] #we can use len(res)
#temp_choice = res['results']
if total > 1:
    print(f"There are {total} Jokes")
    print(choice(res['results'])['joke']) # use temp_choice in place of res['results]
elif total == 1:
    print("There is only one joke")
    print(res['results'][0]['joke'])
else :
    print(f"We cant find any joke with your keyword '{user_input.upper()}'")
