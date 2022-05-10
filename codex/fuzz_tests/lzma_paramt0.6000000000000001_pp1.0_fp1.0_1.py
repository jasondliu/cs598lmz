from lzma import LZMADecompressor
LZMADecompressor.ALGO_X86 = 0
LZMADecompressor.ALGO_LZMA1 = 1
LZMADecompressor.ALGO_DELTA = 2
LZMADecompressor.ALGO_LZMA2 = 3
LZMADecompressor.check = lambda x: None

from plistlib import Data
Data.fromBase64 = lambda x: x.data

from requests import Session
Session.send = lambda x, y: (x, y)

from urllib.request import HTTPCookieProcessor, CookieJar
HTTPCookieProcessor.http_request = lambda x, y: y
HTTPCookieProcessor.http_response = lambda x, y: y
CookieJar.extract_cookies = lambda x, y: None

from xml.dom.minidom import parseString
parseString.parseString = lambda x: x

from xml.etree.ElementTree import XML
XML.XML = lambda x: x

from xml.sax.handler import ContentHandler
ContentHandler.characters = lambda
