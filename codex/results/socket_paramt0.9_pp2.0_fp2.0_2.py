import socket
socket.if_indextoname(3)

socket.if_nametoindex("en0")

import urllib2
for line in urllib2.urlopen("http://baidu.com"):
    print(line.decode().strip())

import urllib
params = urllib.urlencode({"test":"test"})
req = urllib2.Request("https://www.baidu.com",params)
req.add_header("Referer","https://www.baidu.com")
for line in urllib2.urlopen(req):
    print(line.decode().strip())

import urllib2
cj = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cj)
urllib2.install_opener(opener)
urllib2.urlopen("http://www.baidu.com")
print(cj)

import urlparse
result = urlparse.urlparse("http://www.baidu.com/test?test=test")
print
