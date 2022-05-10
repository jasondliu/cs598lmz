import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "spam"
</code>
If I call fun() I get:
<code>&gt;&gt;&gt; fun()
'the string "spam"'
</code>
If I call it from the interactive prompt, I get:
<code>&gt;&gt;&gt; ctypes.CFUNCTYPE(ctypes.py_object)(fun)()
'spam'
</code>
Note that I'm not even using eval. Either way, I get the reference to the string "spam", but the way eval sees it, it seems like a new string. Why?

