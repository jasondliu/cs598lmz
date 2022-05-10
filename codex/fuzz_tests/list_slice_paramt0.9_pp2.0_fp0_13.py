import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback
           ))
lst2=list(lst)     
del a
</code>
i know deleting x causes the callback to be called but i want to know why
trying to delete lst[0] via callback causes:
<code>RuntimeError: weakly-referenced object no longer exists


Unhandled exception in thread started by &lt;function poll_notifier at 0x009E7E68&gt;
Traceback (most recent call last):
  File "C:\Users\sid\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\utils\autoreload.py", line 229, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\sid\AppData\Local\Programs\Python\Python37-32\lib\site-packages\channels\management\commands\runserver.py", line 57, in inner_run
    self.inner_run(parser, options)
  File "C:\Users\sid\AppData\Local\Programs\Python\Python37-32\lib\site
