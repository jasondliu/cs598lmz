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





# 04:34:02.049185 IP 23.97.157.15.443 > 10.21.1.60.26662: Flags [.], ack 13, win 277, length 0
# 04:34:02.049231 IP 10.21.1.60.26662 > 23.97.157.15.443: Flags [P.], seq 13:45, ack 1, win 273, length 32
# http://img.tbcdn.cn/tfscom/TB1bTcGKXXXXXcKaFXXXXXXXXXX (?, 23.97.157.15)
#
# 04:34:02.318238 IP 23.97.157.15.443 > 10.21.1.60.26662: Flags [.], ack 45, win 277, length 0
# 04:34:02.318344 IP 23.97.157.15.443 > 10.21.1.60.26662: Flags [P.], seq 1:17, ack 45, win 277, length 16
# http://img.tbcdn.cn/tfscom
