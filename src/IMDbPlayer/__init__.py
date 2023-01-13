try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    raise Exception("Error loading bs4")

import requests, sys, re, webbrowser

IMDB_FIND ='https://www.imdb.com/find/?q='
MOVIE_URL_BASE = 'https://www.2embed.to/embed/imdb/movie?id='
TV_URL_BASE = 'https://www.2embed.to/embed/imdb/tv?id='
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def main():
    try:
        title = ''.join([i for i in sys.argv[1] if not i.isdigit()])
    except IndexError:
        raise Exception("Usage: name [optional: season] [optional: episode]")
    if any(i.isdigit() for i in sys.argv[1]):
        nums = list(map(int, re.findall(r'\d+', sys.argv[1])))
                   
    imdb_search_url = IMDB_FIND + title.replace(' ', '%20')

    request = requests.get(imdb_search_url, headers=HEADERS)
    data = BeautifulSoup(request.content, 'html.parser')
    ipc_metadata_list = str(data.find_all('ul', attrs={
        'class': re.compile('^ipc-metadata-list.*')
        })[0])
    hrefs = re.findall('href="(.*?)"', ipc_metadata_list)
    imdb_id = re.findall('/([^;]*)/', hrefs[0][1:])[0]

    url = (f'{TV_URL_BASE}{imdb_id}&s={nums[0]}&e={nums[1]}'
           if 'nums' in locals() else f'{MOVIE_URL_BASE}{imdb_id}')
        
    webbrowser.open(url)