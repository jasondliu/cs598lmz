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
print(lst)
</code>
The above example should create a reference cycle (not object graph cycle) which means that 'a' object cannot be gc'ed unless its "c" reference is set to None or the associated weakref object is destroyed.
right?
Anyway, in Python 2.7 I am getting the following problem when trying to run this example:
<code>haf@haf:~/Desktop$ python test.py
** Python 2.7.10 (default, Oct 23 2015, 18:05:06)
:~$
['']
Segmentation fault
</code>
This happens only when the weak reference was used to keep a object in memory (I changed the code to keep a 'a' object "alive" using an ordinary reference in c_ref and this works fine)
Does anybody know why? 
Thank you


A:

The issue you describe is known for Python 2.7
<code>Segmentation fault</code> is a runtime crash and you can read about on the issue tracker, it is caused for example by the following example code
