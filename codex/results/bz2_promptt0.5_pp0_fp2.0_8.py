import bz2
# Test BZ2Decompressor
# decompressor = bz2.BZ2Decompressor()
# f = open('enwiki-latest-pages-articles1.xml-p000000010p000010000-shortened.bz2', 'rb')
# decompressor.decompress(f.read(1000))
# f.close()

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# Retrieves a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
