from bz2 import BZ2Decompressor
BZ2Decompressor()(open(BZ_FILE, 'rb').read()).decode('utf8')

# using the BytesIO class to read the compressed data in memory
import bz2
bz2.BZ2File(BZ_FILE).read().decode('utf8')

import gzip
u = gzip.open(GZ_FILE, 'rt', encoding='utf8').read()
u

u.encode("ascii", "xmlcharrefreplace").decode("ascii")

u

from bs4 import BeautifulSoup
soup = BeautifulSoup(u, 'html.parser')

links = soup.find_all("a")
links[15:20]

str_links = str(links)
str_links[:200]

# parsing and extracting href values from the anchors
soup.find_all("a", href=True)[:10]

links = soup.find_all("a", href=True)

for tag in links:
    print("TAG:", tag)
    print("URL:", tag["href"])
