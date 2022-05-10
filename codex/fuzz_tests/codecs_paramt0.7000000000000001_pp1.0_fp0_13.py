import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

import sys
import re
import requests

from bs4 import BeautifulSoup
from tqdm import tqdm

def get_events(url):
    html = requests.get(url).content.decode(encoding='utf-8', errors='replace_with_space')
    html = re.sub('[\t\n\r]', ' ', html)
    soup = BeautifulSoup(html, 'html.parser')
    event_tags = soup.find_all('div', class_='event-inner-item')
    return [tag.find('a').find('span').text.strip() for tag in event_tags]

def main(argv):
    output_filename = 'events.txt'
    if len(argv) > 1:
        output_filename = argv[1]

    with open(output_filename, 'w') as output_file:
        output_file.write('\n'.join(get_events('https://www.worldathletics.org/calendar
