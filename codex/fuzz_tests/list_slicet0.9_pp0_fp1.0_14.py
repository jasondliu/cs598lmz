import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print hex(len(keepali0e))
print keepali0e[:5]

c=[(a,b) for (a,b) in t.groups()]

import urllib
import urllib3
def test():
    http=urllib3.PoolManager()
    url="http://km.cqupt.edu.cn/Home/Sys/verifyCode?2013.09.19"
    flag=0
    try:
        pic=http.urlopen('GET',url,preload_content=False)
        f=open('%.jpg'%flag,'wb')
        while 1:
            data=pic.read(1024)
            if not data:
                break
            f.write(data)
        f.close()
        pic.close()
    except Exception,e:
        print e
    print 'i am ok'
def test1(url):
    http=urllib3.PoolManager()
    print url
    try:
        pic=http.urlopen('GET',url,preload_content=False)
       
