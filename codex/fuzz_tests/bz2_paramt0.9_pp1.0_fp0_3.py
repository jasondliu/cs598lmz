from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(ResponseIncomplete: 2 bytes left)
</code>
I am new to BeautifulSoup, but this appears to be a problem with ResponseIncomplete: 2 bytes left.  I'm sure there's more from the response I need to catch, but how do I actually get the data from the response object?
Thanks!


A:

I was able to find a solution.
I saved the response.iter_content(1000) to a new file then used BeautifulSoup on the text. 
<code>import requests
from bs4 import BeautifulSoup
from bz2 import BZ2File
from bz2 import BZ2Decompressor

response = requests.get(url,stream=True)

with open('file.txt', 'wb') as out_file:
    for chunk in response.iter_content(1000):
        out_file.write(chunk)


    input_file = BZ2File('file.txt')
    xml = ''.join(input_file.readlines())
    soup = BeautifulSoup(xml, 'lxml')
</code>

