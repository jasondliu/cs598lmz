from types import FunctionType
list(FunctionType(__import__('numpy').ufunc.reduce)(lambda x,y: (x if isinstance(x,(str,int)) else x[0],y),[(0.0,0),(1.0,1),(2.0,2)],None))

# The following is equivalent to the first block of code above:
list(reduce(lambda x,y: (x if isinstance(x,(str,int)) else x[0],y),[(0.0,0),(1.0,1),(2.0,2)],None))
</code>
The first example gives the expected output
<code>[1, 2, 3]
</code>
while the second example gives the following incorrect output:
<code>[(0.0, 0), (1.0, 1), (2.0, 2)]
</code>
As you can see, something is wrong with the usage of <code>reduce</code> in
<code># This is the correct line.
list(FunctionType(__import__('numpy').ufunc.reduce)(lambda x,
