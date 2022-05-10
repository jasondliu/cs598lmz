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
print(len(keepali0e))
#用于输出指定最大深度的内建对象的内存使用情况，对象地址是以十六进制表示的
import gc,psutil
gc.set_debug(gc.DEBUG_LEAK)
for x in range(3):gc.collect()
print(psutil.Process(os.getpid()).memory_info().rss)
#print(gc.dump_rpycobjects(max_depth=3))
gc.collect()
print(psutil.Process(os.getpid()).memory_info().rss)
gc.set_debug(None)
#python2.7标准库中，weakref.ref类能创建一个引用对象，当它指向的对象
