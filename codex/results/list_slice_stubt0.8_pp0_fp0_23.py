import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del keepalive
lst.append(a.c)
lst.append(a)
lst.append(str())
lst.append(lst)
lst.append(lst)
lst.append(callback)
del keepalive
wea0ref.proxy(lst,callback)

# 参考链接: https://www.freebuf.com/articles/system/177893.html
# 参考链接: https://github.com/pwndbg/pwndbg/blob/master/examples/one-gadget.py

# # 如果遇到此错误: one_gadget: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.27' not found (required by one_gadget)
# # 获取较新的 libc.so.6
# #
