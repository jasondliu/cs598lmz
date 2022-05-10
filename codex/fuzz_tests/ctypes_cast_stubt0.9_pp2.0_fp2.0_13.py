import ctypes
ctypes.cast(0, ctypes.py_object).value = 'a'
</code>
Or if you are not particularly interested in doing bad things and just have no idea how it works:
<code>class Foo(object):
    pass
a = Foo()
a.value = 'a'
</code>
The positive side of all this is that when you create your x86/x64 specific applicaton it is indeed running that much faster at the moment when it is managing your objects.

