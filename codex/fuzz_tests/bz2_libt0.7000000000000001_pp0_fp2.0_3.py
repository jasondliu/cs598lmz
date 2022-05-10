import bz2
bz2.decompress(data)

# Q2.2
f = bz2.BZ2File('file.bz2','w')
f.write(data)
f.close()

# Q2.3
import urllib.parse
import urllib.request
import re

# Q2.3.1
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

# Q2.3.2
data = urllib.parse.urlencode({'nothing':'12345'})
#data = data.encode('utf-8')
data = data.encode('ascii')
req = urllib.request.Request(url,data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
the_page = the_page.decode('utf-8')
print(the_page)

# Q2.3.3
the_page.split(" ")[-1]

# Q2.4
# Q2.4
