import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback)
print('keepalive'.c)


#=====================网络请求==============================

import socket
hostname='baidu.com'
addr=socket.gethostbyname(hostname)
print(addr)

import httplib
conn=httplib.HTTPConnection('www.python.org')
conn.request('GET','/')
r1=conn.getresponse()
print(r1.status,r1.reason)
data1=r1.read()
print(len(data1))

import urllib
u=urllib.urlopen('http://www.python.org')
#print(u.read())
#import urllib2
#req=urllib2.Request('http://www.python.org')
#response=urllib2.urlopen(req)
#the_page=response.read()
#print(the_page)
#import urllib
params = urllib.urlencode({'spam': 1, 'eggs': 2, '
