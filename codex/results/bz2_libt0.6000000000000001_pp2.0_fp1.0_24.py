import bz2
bz2.decompress(open('tmp/pages.xml.bz2', 'rb').read())

from xml.etree import cElementTree as ET
from collections import Counter
from tqdm import tqdm

tree = ET.iterparse('tmp/pages.xml.bz2', events=('start', 'end'))
text = []
for event, elem in tqdm(tree):
    if elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}page':
        if event == 'start':
            title = elem.find('{http://www.mediawiki.org/xml/export-0.10/}title').text
            text.append(title)
        elif event == 'end':
            elem.clear()

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# nltk.download('punkt')
# nltk.download('stopwords')

stop_words = set(stopwords.words('russian
