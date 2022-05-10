import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a.d=lst
while keepali0e:
	print("Loop")
	del lst[:]
	lst.append(str())
	time.sleep(0.01)

#计算代码运行时间
import time
start=time.time()
time.sleep(1)
print("执行时间：%s"%(time.time()-start))

#使用模块
import sys
for i in sys.argv:
	print(i)
print("python的路径：%s"%sys.path)

#引入模块
import sys
sys.path.append("D://python//lib")
print("python的路径：%s"%sys.path)

#函数
def fib(n):
	a,b=0,1
	while a<n:
		print(a,end=" ")
