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
and the following command line:
<code>C:\Python&gt;python -m cProfile -s cumulative test.py
</code>
The output of the above command is:
<code>        7 function calls in 3.000 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.000    3.000 test.py:1(&lt;module&gt;)
        1    0.000    0.000    3.000    3.000 {built-in method builtins.exec}
        1    0.000    0.000    3.000    3.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    3.000    3.000 {method 'append' of 'list' objects}
        1    3.000    3.000    3.000    3.000 {method 'append' of 'list' objects}
        1    0.000   
