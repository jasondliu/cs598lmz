import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
printf = ctypes.CDLL(None).printf

# http://stackoverflow.com/questions/17982277/ctypes-attach-function-to-slot
printf.__dict__['__call__'].__dict__['__call__'].__func__(printf, 'Hello, world')
</code>
The error message for the line with the comment looks like this:
<code>c:/Python33/lib/ctypes/__init__.py:552: in __call__
    return self._function(*args)
TypeError: CFUNCTYPE object with invalid number of arguments: 1 expected, got 0
</code>
I've tried replacing <code>None</code> with <code>[]</code> and nothing happens.


A:

Figured it out.
<code>import ctypes
CFUNTYPE = ctypes.CFUNCTYPE(None)
printf = CFUNTYPE(('printf','libc.so.6'))
printf("Hello, world")
</code>
Edited to include a better comment. As @stdcall says, this
