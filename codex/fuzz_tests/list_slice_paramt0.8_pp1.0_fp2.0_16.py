import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
ldquo;callbackrdquo; =callback
keepali0e.append(weakref.ref(ldquo;callbackrdquo;,callback))
keepali0e.append(weakref.ref(lst))
</code>
rst=
 

as this is the situation you will get if you using Tkinter (in Python) and a widget is deleted, but there are still references to this widget, which will never be garbage collected.

