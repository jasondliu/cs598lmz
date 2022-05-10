from types import FunctionType
list(FunctionType([], []).__dict__.items())

# Output:
[('_call_', &lt;function __main__.&lt;lambda&gt;&gt;),
 ('__closure__', None),
 ('__code__', &lt;code object &lt;lambda&gt; at 0x7f7f26245358, file "&lt;stdin&gt;", line 1&gt;),
 ('__defaults__', None),
 ('__dict__', &lt;attribute '__dict__' of 'function' objects&gt;),
 ('__doc__', None),
 ('__get__', &lt;method '__get__' of 'function' objects&gt;),
 ('__globals__', {'FunctionType': &lt;class 'type'&gt;,
                  '__name__': '__main__',
                  '__doc__': None,
                  '__package__': None,
                  '__loader__': &lt;_frozen_importlib_external.SourceFileLoader object at 0x7f7f27f3ca58&gt;,
                  '__
