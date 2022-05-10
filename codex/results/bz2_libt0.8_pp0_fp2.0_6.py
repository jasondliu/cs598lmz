import bz2
bz2.decompress(test_data.read())
# open('test_data.json', 'r').read()
from urllib.request import urlopen
test_data = urlopen('https://tinyurl.com/t8rc3br')
bz2.decompress(test_data.read())

from bz2 import decompress
from io import BytesIO
from urllib.request import urlopen
test_data = urlopen('https://tinyurl.com/t8rc3br')
decompressed_file = BytesIO(decompress(test_data.read()))
decompressed_file.read()

from bz2 import decompress
from io import BytesIO
from urllib.request import urlopen
test_data = urlopen('https://tinyurl.com/t8rc3br')
decompressed_file = BytesIO(decompress(test_data.read()))
import json
json.load(decompressed_file)

import json
from bz2 import decompress
from io import BytesIO
from ur
