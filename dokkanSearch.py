#!/usr/bin/python3.9
# type ./dokkanSearch.py keyword in the command line (keyword == what you want to search for)

import requests, bs4, sys, webbrowser

# gets dokkan wiki search
res = requests.get(f'https://dbz-dokkanbattle.fandom.com/wiki/Special:Search?query={sys.argv[1:]}&scope=internal&navigationSearch=true')

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# selects links with the class 'unified-search_result_title'
links = soup.select('a.unified-search__result__title') 

numOpen = min(2,len(links))
# gets top two links
for i in range(numOpen) :
    urlToOpen = links[i].get('href')
    print(f'Opening {urlToOpen}')
    webbrowser.open(urlToOpen)