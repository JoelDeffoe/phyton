import csv
import requests
from bs4 import BeautifulSoup
from random import randint

# page = []
# # https://www.anime-planet.com/manga/all?sort=title&order=asc&page=2
# for i in range(1, 1193):
url = 'https://www.anime-planet.com/manga/all?sort=title&order=asc&page={}'


def getmanga(url):

    for link in [url.format(page) for page in range(1, 11)]:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'lxml')
        manga_list = soup.find('ul', class_='cardDeck cardGrid')

        # image = []
        name = []
        description = []
        for n in manga_list:
            # manga name
            name = n.h3

            # detailed
            description = n.a.attrs['title']

            # manga image
            # image = n.img

            writer.writerow(name, description)
            print(description)


if __name__ == "__main__":

    with open('tabularitem.csv', 'w', newline="", encoding="utf-8") as infile:
        writer = csv.writer(infile)
        getmanga(url)
