from types import FunctionType
list(FunctionType(lambda: 0, {}, '__lambda__', (), None).__code__.co_names)
# ['__lambda__']
</code>
If you want to get a list of the names of all the functions defined in a module, you'll have to look in the <code>__dict__</code> of the module (or elsewhere, depending on how the function was defined):
<code>&gt;&gt;&gt; import types
&gt;&gt;&gt; types.__dict__
{'__name__': 'types', '__file__': '/usr/lib/python2.7/types.pyc', 'StringTypes': (&lt;type 'str'&gt;,), 'DictProxyType': &lt;type 'dictproxy'&gt;, 'GeneratorType': &lt;type 'generator'&gt;, '__path__': ['/usr/lib/python2.7'], 'TracebackType': &lt;type 'traceback'&gt;, 'TypeType': &lt;type 'type'&gt;, 'XRangeType': type(xrange(
