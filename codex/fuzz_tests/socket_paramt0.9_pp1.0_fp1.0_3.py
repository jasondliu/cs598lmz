import socket
socket.if_indextoname('https://www.google.com/search?q=python+interview+questions&oq=python+interview+questions&aqs=chrome..69i57.19682j0j8&sourceid=chrome&ie=UTF-8')

import urllib
url = 'https://www.google.com/search?q=python+interview+questions&oq=python+interview+questions&aqs=chrome..69i57.19682j0j8&sourceid=chrome&ie=UTF-8'
urllib.parse.urlparse(url)
urllib.parse.urlparse(url).hostname  #hostname without port number

import urllib
import urllib.request as ulib
raw_data = ulib.urlopen('http://google.com/search?q=python+interview+questions&oq=python+interview+questions&aqs=chrome..69i57.19682j0j8&sourceid=chrome&ie=UTF-8')
print(raw_data.read())
