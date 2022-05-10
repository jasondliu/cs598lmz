import bz2
bz2.__name__

print('bz2 version is {}'.format(bz2.__version__))

import urllib.request

url = 'https://docs.python.org/'+\
    '3/library/functions.html#open'

response = urllib.request.urlopen(url)
webpage = response.read()
print(type(webpage), len(webpage))

# first N bytes
N = 300
webpage_bz2 = bz2.compress(webpage)[:N]
print(type(webpage_bz2), len(webpage_bz2))

webpage2 = bz2.decompress(webpage_bz2)
print(type(webpage2), len(webpage2))

with open('open_function.html.bz2', 'wb') as f:
    f.write(webpage_bz2)

with open('open_function.html', 'wb') as f:
    f.write(webpage)

with bz2.open
