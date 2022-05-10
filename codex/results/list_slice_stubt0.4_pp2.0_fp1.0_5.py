import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive.append(a)
lst[0]=a
weakref.ref(a,callback)
del a
del keepalive
</code>
This is the code that I am using to test the garbage collector.
It is a simplified version of the code in the question I posted.
I am using Python 2.7.6 on Windows 7.
I am using the following command to run the program:
python -m cProfile -o out.txt test.py
The output of the cProfile is as follows:
<code>         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 &lt;string&gt;:1(&lt;module&gt;)
        1    0.000    0.000    0.000    0.000 test.py:1(&lt;module&gt;)
        1    0.000    0.000    0.000   
