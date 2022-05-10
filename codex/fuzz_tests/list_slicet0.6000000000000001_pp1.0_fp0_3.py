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
Then, if you're using Python 2.7 or Python 3.2, you can use the <code>idlelib.idle_test.regrtest</code> test runner to run this and see what happens:
<code>$ python -m idlelib.idle_test.regrtest -R 2:3 test_weakrefleak.py
</code>
On my machine, this prints:
<code>2: test_weakrefleak
</code>
and exits with an exit code of 2, indicating a test failure.

