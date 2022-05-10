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
Output:   
<code>&gt;&gt;&gt; py_leak.py --leak

Traceback (most recent call last):
  File "/home/antocuni/PyLeak/py_leak.py", line 374, in &lt;module&gt;
    test_leak_cycle()
  File "/home/antocuni/PyLeak/py_leak.py", line 369, in test_leak_cycle
    run_test(cycles)
  File "/home/antocuni/PyLeak/py_leak.py", line 141, in run_test
    if is_leak(fn):
  File "/home/antocuni/PyLeak/py_leak.py", line 169, in is_leak
    block = gc.collect()
RuntimeError: GC object already tracked
</code>


A:

Yes, there is a leak.  
I ran your program with the <code>-R</code> command line option, which dumps out the references at each collection.  Here is the
