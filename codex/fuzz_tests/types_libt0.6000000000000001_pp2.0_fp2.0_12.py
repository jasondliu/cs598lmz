import types
types.MethodType(__builtin__.__import__, None)

# This is the code I want to run
import sys
sys.modules['__builtin__'].__dict__['__import__'] = None

# After this, I can't import anything
import types
types.MethodType(__builtin__.__import__, None)
# NameError: name '__builtin__' is not defined
</code>
I am using Python 2.6.4.


A:

A better way to disable <code>__import__</code> is to use the <code>imp</code> module.
<code>import imp
imp.acquire_lock()
del __builtins__["__import__"]
</code>
<code>__import__</code> is a built-in function.  It's not in your modules' <code>__dict__</code>s.  It's in the <code>__builtins__</code> of the module.  In Python 2, <code>__builtins__</code> is a dictionary.  In Python 3, it's a module
