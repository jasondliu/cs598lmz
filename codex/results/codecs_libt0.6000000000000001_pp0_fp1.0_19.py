import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import requests
import bs4
from bs4 import BeautifulSoup
import re
import pandas as pd

#Página a scrapear
page = requests.get('https://www.spanishdict.com/traductor/perro')

#Parseo de la página
soup = BeautifulSoup(page.text, 'html.parser')

#Creación de función para obtener las palabras
def get_vocabulary(soup):
	vocabulary = []
	for index, tag in enumerate(soup.find_all('a', {'class': 'dict-result-spanish-target'})):
		vocabulary.append(tag.text)
	return vocabulary

#Creación de función para obtener los significados
def get_meanings(soup):
	meanings = []
	for index, tag in enumerate(soup.find_all('div', {
