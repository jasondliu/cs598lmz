import select
# Test select.select() using selectors module.
import asyncio
from aiohttp import ClientSession
import binascii

TIMEOUT = 5 # seconds
TARGET_HOST = "127.0.0.1"
TARGET_PORT = 4242
TARGET_URL = "http://{}:{}".format(TARGET_HOST, TARGET_PORT)
HEADERS = {
    'Cache-Control': 'max-age=0',
    'Accept-Language': 'en-US,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.google.com/',
}
