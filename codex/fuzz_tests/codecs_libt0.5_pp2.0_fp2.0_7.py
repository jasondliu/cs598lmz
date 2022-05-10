import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import re
import urllib
from bs4 import BeautifulSoup
import requests
import json
import time

def clean(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\r', ' ', text)
    text = re.sub(r'\t', ' ', text)
    text = re.sub(r'\xa0', ' ', text)
    text = re.sub(r'\u3000', ' ', text)
    text = re.sub(r'\u202f', ' ', text)
    text = re.sub(r'\u2009', ' ', text)
    text = re.sub(r'\u200a', ' ', text)
    text = re.sub(r'\u200b', ' ', text)
    text = re.sub(r'\u200c', ' ', text)
    text = re.sub(r'\u200d
