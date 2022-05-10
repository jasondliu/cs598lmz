import bz2
# Test BZ2Decompressor
cd1 = bz2.BZ2Decompressor()
data1 = cd1.decompress(compressedFile)
print(len(data), len(data1))

print(data1.decode())
'''

# Advanced: Multithreaded Decompression of Multiple BZ2 Files
'''
import bz2
import concurrent.futures

def from_bz2(filename: str) -> str:
    with bz2.BZ2File(filename) as f:
        return f.read().decode()

filenames = ['filename1', 'filename2', 'filename3']

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(from_bz2, filenames)
    for result in results:
        print(result)
'''

# Advanced: Querying External Services
'''
from urllib import request

class Weather:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
