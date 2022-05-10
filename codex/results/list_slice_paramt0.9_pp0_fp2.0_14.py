import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, lambda a:callback(lst)))
</code>
The above code gives me a <code>SystemError: NULL result without error in PyObject_Call</code> error. 
How can I prevent this from happening?
I know I can change the code in a way where I won't create a circular reference but the question is not about the usability of circular references in this example, but about how to prevent the error from happening.

