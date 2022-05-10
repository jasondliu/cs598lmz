import bz2
bz2.decompress(r.content)

# you can use urllib.request to send requests
import urllib.request
req = urllib.request.Request(url, method='HEAD')
r = urllib.request.urlopen(req)
# you can use urllib.parse to parse the url
import urllib.parse
url = 'https://www.google.com.hk/search?q=python'
pr = urllib.parse.urlparse(url)
pr

# use `urllib.request` to request https, need to install ssl
import urllib.request
# create the object, assign it to a variable
u = urllib.request.urlopen('https://www.python.org')
type(u)

# read the file-like object
u.read()

# use urllib.parse to parse the url, create a new request
import urllib.request
import urllib.parse
url = 'https://www.google.com.hk/#newwindow=1&safe=strict&q=
