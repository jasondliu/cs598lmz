import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:
    print(lst)
    time.sleep(0.1)

#第一次打印：['\x00']
#第二次打印：['\x00']
#第三次打印：['\x00']
#第四次打印：['\x00']
#第五次打印：['\x00']
#第六次打印：['\x00']
#第七次打印：['\x00']
#第八次打印：['\x00']
#第九次打印：['\x00']
#第十次打印：['\x00']
#第十一
