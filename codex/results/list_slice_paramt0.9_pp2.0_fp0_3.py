import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
# del a.c
print (a)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 激活回调函数  callable object  实参对象 数字对象
# weakref.finalize() 生成最终回调函数  最终回调函数避免没有对象被回收
import weakref
def close_file(file):
    print( "file to be closed",file)
import gc
f = open(r'c:/1.txt')
# 在文件一被回收时自动执行close_file
weakref.finalize(f, close_file,f)
del f
# 显示
