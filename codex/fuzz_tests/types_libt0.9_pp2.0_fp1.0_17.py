import types
types.MethodType(func, [float, float])
</code>
TypeError: argument 1 must be code, not list
The first two lines are okay, but the third is for creating a new method, and
I don't understand why the example uses a list there. how does the third line mean?
Thanks a lot!


A:

Change it to:
<code>func = MethodType(my_abs, float)
# or
func = my_abs
</code>
The third argument is the class to bind to.

