import requests
from bs4 import BeautifulSoup
import csv


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL).text

soup = BeautifulSoup(response, 'html.parser')

films = soup.select(selector='h3')

films_list = []

for film in films:
    films_list.append(film.getText())

new_arr = list(reversed(films_list))

print(new_arr)

with open('GFG', 'w',encoding='utf-8') as f:
    write = csv.writer(f)
    write.writerow(new_arr)