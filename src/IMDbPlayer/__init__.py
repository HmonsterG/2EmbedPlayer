try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    raise Exception("Error loading bs4")

__version__ = '1.0.0'

IMDB_FIND ='https://www.imdb.com/find/?q='
MOVIE_URL_BASE = 'https://www.2embed.to/embed/imdb/movie?id='
TV_URL_BASE = 'https://www.2embed.to/embed/imdb/tv?id='
HEADERS = {'User-Agent': 'Mozilla/5.0'}
