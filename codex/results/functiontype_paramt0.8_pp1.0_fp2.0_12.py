from types import FunctionType
list(FunctionType(foo, globals()).__globals__.items())
# [('__name__', '__main__'), ('__doc__', None), ('__package__', None), 
#  ('__loader__', &lt;class '_frozen_importlib.BuiltinImporter'&gt;), 
#  ('__spec__', None), ('__annotations__', {}), 
#  ('__builtins__', &lt;module 'builtins' (built-in)&gt;), 
#  ('__file__', '/Users/jari/Documents/python/t.py'), 
#  ('__cached__', None), ('foo', &lt;code object foo at 0x106a47fc0, file "t.py", line 1&gt;)]
</code>
In my opinion, the first approach seems to make more sense, but what is the reason that the second one is supported?
Edit: I already know of the <code>__closure__</code> attribute, but I don't think that this is relevant for my question. I'm interested in why the <code>glob
