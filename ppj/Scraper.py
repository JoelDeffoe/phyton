import csv
import requests
from bs4 import BeautifulSoup
from random import randint

# get websit


r = requests.get('https://www.anime-planet.com/manga/all?sort=title&order=asc')
soup = BeautifulSoup(r.text, 'lxml')


# get name if eatche manage of the first page
manga_name = soup.find_all('h3')
manga_image = soup.find_all('img')

# len(manga_name)

main_name = []
for n in manga_name:
    main_name.append(n.text)
    print(n.text)


print(main_name)

# convert into a csv file
# print(','.join(main_name).encode('utf-8'))
# csv_writer.writerow([main_name])
# filename = "mangatest.csv"
# csv_writer = csv.writer(open(filename, 'w'))

if __name__ == "__main__":
