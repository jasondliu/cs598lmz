from lzma import LZMADecompressor
LZMADecompressor().decompress(b"\x00\x01\x02")

# extraction
import json
from bz2 import BZ2File

def bz2_decode(file):
    with BZ2File(file) as f:
        data = f.read()
    return data.decode("utf-8")

def json_loads(data):
    return json.loads(data)

def process(file):
    data = bz2_decode(file)
    data = json_loads(data)
    return data

file = "ch04-data/py3/data.json.bz2"
