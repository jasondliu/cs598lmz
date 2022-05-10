from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
"""

"""
from gzip import decompress
decompress(data)
"""

response = requests.get("http://www.pythonchallenge.com/pc/def/package.php")
# print(response.text)

"""
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://www.pythonchallenge.com/pc/return/evil2.gfx').read()

gfx = open('evil2.gfx', 'wb')     # open binary file for writing
gfx.write(img)
gfx.close()
"""

"""
with open('evil2.gfx', 'rb') as f:
    data = f.read()
"""

"""
open('evil2.jpg', 'wb').write(data[0::5])
open('evil2.jpg', 'wb').write(data[1::5])
open('evil2.jpg', 'wb').write(data[2::5])
open('evil2.jpg', '
