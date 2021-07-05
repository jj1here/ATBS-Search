#!/usr/bin/python3.9
# type ./search.py keyword in the command line (keyword == what you want to search for)

import requests, bs4, sys, webbrowser

print("Searching...")
#'https://google.com/search?q='
res = requests.get('https://pypi.org/search/?q='+''.join(sys.argv[1:]))
res.raise_for_status()
# print(res.text)
# retrieve top links
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# open a new tab for each
linkElems = soup.select(".package-snippet")

# print(linkElems)
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org'+ linkElems[i].get('href')
    print(urlToOpen)
    print('Opening',urlToOpen)
    webbrowser.open(urlToOpen)

