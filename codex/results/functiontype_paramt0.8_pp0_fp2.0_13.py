from types import FunctionType
list(FunctionType(lambda x: x**2, globals(), 'f')())
</code>
returns
<code>[f]
</code>
It is just a function object but it still appears in a list. Now what I would like is a way to check if an object can appear in a list and not just the fact that it is a function.
EDIT: It seems that the usage of this trick would be quite rare and the fact that this does not work on classes is quite important so I will just forget about it and make sure that my loop always starts with an iterable.


A:

You could try something like
<code>if isinstance(obj, list):
    print "it's list"

if isinstance(obj, tuple):
    print "it's tuple"

if isinstance(obj, (list, tuple)):
    print "it's list or tuple"
</code>

