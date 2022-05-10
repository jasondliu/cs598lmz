import codecs
codecs.register_error('surrogateescape', codecs.surrogateescape_error)

import requests
from lxml import html, etree
import re
from io import StringIO, BytesIO
from collections import Counter
from datetime import datetime
import time

def get_blob(url):
  time.sleep(1)
  html_bytes = requests.get(url).content
  return html.fromstring(html_bytes)

def parse_date(date_string):
  match = re.match('([0-9]{4})-([0-9]+)-([0-9]+)( ([0-9]+):([0-9]+):([0-9]+))?([A-Z]*)?', date_string)
  if match is None:
    print("failed to match date")
    return None
  gs = match.groups()
  year = int(gs[0])
  month = int(gs[1])
  day = int(gs[2])
  hour = 0
  minute = 0
  second = 0
  if gs[3] is not None
