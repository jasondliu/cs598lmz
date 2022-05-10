import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=lst
lst.append(keepalive)
lst.append(a)
lst.append(a)
keepalive=weakref.ref(a,callback)

6.如何用Python代码判断一个服务器是上线还是下线
ping就可以，假如你有将要测试服务器ip以及端口，则可以
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(5)
if not s.connect_ex(("服务器ip",端口)):
 print("host_name is up!")
else:
 print("host_name is down!")

7.模块之间的循环引用问题
Python
