import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
a = fun.__code__.co_varnames
</code>
<code>&gt;&gt;&gt; a
('self', 'args', 'kwargs', '__code__', '__defaults__', '__closure__',
 '__globals__', '__annotations__', '__kwdefaults__', '__call__', '__dict__',
 '__slots__')
</code>
My question: What is the meaning of <code>__annotations__</code>?
<code>&gt;&gt;&gt; fun.__annotations__
{'args': &lt;class 'ctypes._CArgObject'&gt;, 'self': &lt;class 'ctypes._CFuncPtr'&gt;, 'kwargs': &lt;class 'ctypes._CFuncPtr'&gt;}
&gt;&gt;&gt; fun.__dict__
mappingproxy({'__self__': &lt;__main__.CFUNCTYPE_PTR object at 0x7fd58601ef08&gt;
