import socket
socket.if_indextoname('80')
socket.if_nametoindex('lo')

socket.gethostbyname("www.baidu.com")
"""

"""
urlparse
urllib.parse

from urllib import parse
parse.urlparse("http://www.baidu.com/index.html;user?id=5#comment")

parse.urlunparse(['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment'])

parse.urlsplit("http://www.baidu.com/index.html;user?id=5#comment")

parse.urlunsplit(['http', 'www.baidu.com', 'index.html', 'a=6', 'comment'])

parse.urljoin('http://www.baidu.com', 'FAQ.html')

parse.urlencode({'name':'jack', 'age':'23'})
"""
"""
urllib.request
\
from urllib import request
req = request.Request('http://www.d
