'''
Program that grabs a url of a picture that you specify
Made by Luke Myers(.aka bahbooshka)
'''

from bs4 import BeautifulSoup
import requests
import random


while True:
    ## Gets input from the user of what the search is
    search = input('Search: ')

    ## sets url
    URL = ('https://www.google.com/search?hl=en&tbm=isch&source=hp&biw=1366&bih=639&ei=sFfVW7CaJJK8sAW-2rfwBQ&q={0}&oq={1}&gs_l=img.3..35i39j0l9.2100.2323..2445...0.0..0.56.162.3......2....1..gws-wiz-img.....0.qY74Fu4zAFQ#imgrc=-hUfSvHcftRrVM:').format(search,search)

    ## gets the pages text
    url = requests.get(URL).text
    soup = BeautifulSoup(url, "html.parser")

    ## creates a list
    images = []

    ## finds all images
    for img in soup.findAll("img"):
        images.append(img.get("src"))

    ## gets a random picture and prints it
    rndmImage = random.randint(0, 5)
    print('\n{}\n'.format(images[rndmImage]))
