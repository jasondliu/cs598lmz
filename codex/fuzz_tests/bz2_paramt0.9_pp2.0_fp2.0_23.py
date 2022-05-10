from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(paths_content3.encode('utf-8'))

# bs4, pandas and numpy libraries initialized
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# Reading the filtered html and soupifying it
mw_soup = BeautifulSoup(paths_content, 'html')
# Parsing all the content by tag table
mw_table = mw_soup.find('table', attrs={'class':'wikitable sortable plainrowheaders'})

# Extracting the headers
mw_headers=[]
column_names = mw_table.find('tr')
for header in column_names:
    mw_headers.append(header.get_text().strip())

# Extracting the all the content data
mw_data = []
mw_rows = mw_table.find_all('tr')
for row in mw_rows:
    mw_data.append([t.get_text().strip() for t in row.find_all('td')
