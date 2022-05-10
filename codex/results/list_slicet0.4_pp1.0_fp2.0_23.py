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
</code>
This is a minimal example of the problem.
The problem is that when I run this code, I get a list of lists with one element in each list, the string <code>''</code>.
I would have expected to get a list of lists with one element in each list, the string <code>''</code>, and then an empty list.
I am using Python 2.7.3.
I am using Ubuntu 12.04.
I am using 64-bit.
I am using the Python IDLE.
I am using the default Python installation.
I am using the default Python IDLE installation.
I am using the default Python IDLE configuration.
I am using the default Python IDLE configuration settings.
I am using the default Python IDLE configuration settings values.
I am using the default Python IDLE configuration settings values options.
I am using the default Python IDLE configuration settings values options preferences.
I am using the default Python IDLE configuration settings values options preferences settings.
I am using the default Python IDLE configuration settings values options preferences settings values.
I am using the default Python IDLE configuration settings values options preferences settings values options.
I
