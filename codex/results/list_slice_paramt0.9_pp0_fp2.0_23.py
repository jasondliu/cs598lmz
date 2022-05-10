import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
for j in range(2):
    print(list(list(globals().items())[x][0] for x in range(len(globals())-1)))
    print(list(lst))
    print(list(list(globals().items())[x][1] for x in range(len(globals())-1)))
    print(list(lst))
print(lst)
</code>
This prints
<code>['str()']
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'callback', 'keepali0e', 'lst', 'weakref', 'x']
[None, None, None, None, None, None, None, None, None, &lt;__main__.A object at 0x00D27B10&gt;, &lt;function callback at 0x02528DC0&gt;,
