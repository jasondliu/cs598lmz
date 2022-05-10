import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a.c,callback))
del a
gc.collect()
</code>
I get the error:
<code>Traceback (most recent call last):
  File "C:\Python27\lib\ctypes\test\test_weakref.py", line 38, in &lt;module&gt;
    gc.collect()
  File "C:\Python27\lib\weakref.py", line 339, in __call__
    self.callback(*self.args, **self.kwargs)
  File "C:\Python27\lib\ctypes\test\test_weakref.py", line 34, in callback
    del lst[0]
  File "C:\Python27\lib\weakref.py", line 322, in __init__
    self.push(key, self)
  File "C:\Python27\lib\weakref.py", line 145, in append
    self.data.append(ref(key, self))
  File "C:\Python27\lib\weakref.py", line 84, in __init__
