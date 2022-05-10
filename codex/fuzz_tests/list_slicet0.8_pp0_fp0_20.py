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
"".join(keepali0e[0])()
del keepali0e
"".join(lst[0])()
```
## traceback模块
可以用来输出栈信息，以异常处理的方式传递字符串
```python
raise ValueError,"我是异常消息"
tb=sys.exc_info()[2]
print(traceback.extract_tb(tb))
print(traceback.format_exc())
print(traceback.format_stack())
traceback.print_exc()
traceback.print_stack()
```
## dis模块
可以用来输出字节码，改变字节码的结构，然后通过eval或者exec动
