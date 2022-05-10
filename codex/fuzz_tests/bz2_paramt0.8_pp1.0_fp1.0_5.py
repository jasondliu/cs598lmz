from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

#/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
import codecs
import re
import requests
import sys
from bs4 import BeautifulSoup
from bz2 import BZ2Decompressor

# URL for the page on Wikipedia containing the content of the book
url = 'http://en.wikipedia.org/wiki/The_Adventures_of_Sherlock_Holmes'

# Character encoding for the HTTP request.
# This should be set to the same value as the <meta> tag in the Wikipedia
# article. This is optional. If it is excluded, requests will try to
# determine the encoding, and it usually gets it right.
encoding = 'utf
