import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0,2,3
print fun()
</code>
Please, explain how to return the tuple in the correct way.
Sorry for my english, if you find mistakes, just tell :)
The idea was, that I had to create the scheme of an N-queens problem. I had to use classes, methods and all other things, that we learned in the university. I had to pass the test results up, so I passed them in a tuple and I wanted to explained, why I can't do it.  


A:

Python 3 has added <code>Py_BuildValue</code>. You ought to be able to use that to build a tuple and then convert it to a python object with <code>ctypes.py_object</code>. I'm not sure how you would deal with integers in a way that wouldn't hit the unexpected narrowing issue, though. I guess if everything is an integer you could use <code>PyLong_FromLongLong</code> and pass in your values as 64 bit ints.
There is no built-in conversion from an iterable to a tuple. However, there is an item in PEP 3121 that involves registering a type that
