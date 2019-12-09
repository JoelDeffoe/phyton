## working bas code 

import csv
import requests
from bs4 import BeautifulSoup
from random import randint

#defin url
url = 'https://www.anime-planet.com/manga/all?sort=title&order=asc&page={}'

### get an drop nam in the csv file 
def getmanga(url):
    # get alle the page url of the web sit 
    for link in [url.format(page) for page in range(1, 1193)]:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'lxml')
        manga_name = soup.find_all('h3')
        #get alle the name of the web sit 
        main_name = []
        for n in manga_name:
            main_name.append(n)
            print(n.text)
            writer.writerow(n)


if __name__ == "__main__":

    with open('tabularitem.csv', 'w', newline="", encoding="utf-8") as infile:
        writer = csv.writer(infile)
        getmanga(url)
