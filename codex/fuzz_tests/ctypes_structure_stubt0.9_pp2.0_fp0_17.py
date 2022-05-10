import ctypes

class S(ctypes.Structure):
    x = a

c = S()
c.x
</code>
The file "test2.py" is
<code>import test1
test1.a
</code>
The issue is that test2.py crash ("abort") because the ctypes.Structure in test1.py need to know the size of 'a' and it's not possible because they are in different file. 
Any solution ? Perhaps something like a class inheritance but with ctypes.Structure ?


A:

I will provide what I think is the best solution to your problem. First of all I recommend reading up on Structures in Cython. 
The solution I will propose will explain how to make the files more modular. We start off by making the file <code>main.pyx</code> which holds the <code>cdef</code> class definitions. Please note that you have to have the <code>cdef</code> function definitions before the <code>def</code> function definitions, as in Cython, the <code>def</code> functions rely on the <code>cdef</code> functions to run and so must come after all the <
