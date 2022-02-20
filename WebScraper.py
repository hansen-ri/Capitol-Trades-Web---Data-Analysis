# https://realpython.com/beautiful-soup-web-scraper-python/
# https://www.youtube.com/watch?v=m-koIYWCaIo

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime


headers = {'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}
datalist = []

def webscrape(pages):
    URL = f'https://www.capitoltrades.com/trades?page={pages}&pageSize=25'
    # "https://app.capitoltrades.com/trades?page={pages}&pageSize=100"
    r = requests.get(URL, timeout=(2, 20), headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    print()
    print(f'Status Code:  {r.status_code}')                                         # Check connection to webpage
    print(f'Page Title: {soup.title.text}')                                         # Check it is the right webpage by displaying title
    # trades = soup.find_all('tr', {'class': 'p-selectable-row ng-star-inserted'})    
    trades = soup.find_all('tr', {'class': 'q-tr'})                                 # Find HTML Element by class name
    print(len(trades))                                                              # Print number of times ^that^ element is on page 

    for item in trades:
        try:
            print()
            firstname = item.find('span', {'class': 'firstName'}).text + " " + item.find('span', {'class': 'lastName'}).text
            print(firstname)
            party = item.find('span', {'class': 'party'}).text
            print(party)
            state = item.find('span', {'class': 'us-state-compact'}).text
            print(state)
            date = item.find('span', {'class': 'format--date-iso'}).find('time')['title']
            print(date)
        except:
            pass

done = False
while done == False:
    print()
    print("WHAT WOULD YOU LIKE TO DO?")
    print('1: Search by keyword (ex: "Nancy Pelosi")')
    print('2: See cumulative trades by party')
    print('3: Extra option')
    answer = input('Please enter your action number: ')

    if answer == "1":
        done = True
        print()
        search = input("What keyword would you like to search? ")
        length = int(input("How many entries of 100 would you like to search?"))
        # for x in range(length):
            # webscrape(search, length)
    elif answer == "2":
        done = True
        pass
    elif answer == "3":
        done = True
        pass
    else:
        print("-------------------------------------------")
        print("Your input was not valid, please try again.")
        print("-------------------------------------------")
        done = False

# check basics
webscrape(10)