import requests
from bs4 import BeautifulSoup
import json

HEADERS = {
	"Accept": "*/*",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

URL = "https://www.gismeteo.ru"
URL_API = "https://www.gismeteo.ru/api/v2/search/searchresultforsuggest/"

def connect(url,headers=HEADERS):
	r = requests.get(url=url, headers=headers)
	return r


def get_city_url(city,url_api=URL_API):
	url = url_api + city
	json_city = json.loads(connect(url).text)
	url_city = json_city['items'][0]['url']
	return url_city


def get_weather_city(url_city,url=URL):
	url_weather = url + url_city + "now/"
	contens = connect(url_weather).content
	soup = BeautifulSoup(contens, 'html.parser')

	temp = soup.find('span', {'class': 'unit unit_temperature_c'}).get_text(strip=True)
	wind = soup.find('div', class_="unit unit_wind_m_s").get_text(strip=True, separator=" ")
	print("\tТемпература =" , temp,"\n" , "\tВетер =" , wind)


def main():
	print("Программа для получения метеорологических данных")
	# action = True
	# while action:
	# 	print("\nВведите ваш город: ")
	# 	enter_city = input()
	# 	if enter_city != " ":
	# 		get_weather_city(get_city_url(enter_city))
	# 		print("Завершить программу ? y/n")
	# 		end_program = input().lower()
	# 		if ((end_program == 'y') or (end_program == 'н')):
	# 			action = False
	print("\nВведите ваш город: ")
	enter_city = input()
	get_weather_city(get_city_url(enter_city))


if __name__ == '__main__':	
	main()
