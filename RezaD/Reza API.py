import requests


input_name = str(input('Enter your name: '))

gender_api = requests.get(f'https://api.genderize.io/?name={input_name}').json()
nationality_api = requests.get(f'https://api.nationalize.io/?name={input_name}').json()

gender = gender_api['gender']
nationality = nationality_api['country'][0]['country_id']

print(f'Gender is: {gender}')
print(f'Nationality ID is probably: {nationality}')