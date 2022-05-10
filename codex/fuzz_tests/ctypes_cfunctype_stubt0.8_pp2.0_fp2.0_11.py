import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print(fun())

widgets.interact(fun)
</code>
This works perfectly with another function:
<code>@FUNTYPE
def fun2(a):
    return a

print(fun2(2))

widgets.interact(fun2)
</code>
The second one works correctly and shows an integer slider. The only reason I want to use the first one is because I want to return another function, but that's not important.
It also works perfectly with a lambda function:
<code>widgets.interact(lambda: 1)
</code>
I don't understand why the first one is not working and I have no idea how to fix it.
This is the full error message:
<code>---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
&lt;ipython-input-9-e8f12d6deae7&gt; in &lt;module&gt;
     12 print(fun())
     13 
---&gt; 14 widgets.interact(fun)
     15 

~/anaconda3/
