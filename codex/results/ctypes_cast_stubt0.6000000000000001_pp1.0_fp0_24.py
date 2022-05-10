import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

#method 2
import sys
sys.getrefcount(obj)
</code>


A:

AFAIK there's no built-in way to do this. You can use the <code>gc</code> module to get a list of all the objects that can be reached from <code>obj</code>, and then you can compare that list to a list of all objects in memory. You can get a list of all objects in memory with a hack like this:
<code>import gc
import inspect

def get_all_objects():
    for obj in gc.get_objects():
        if inspect.isbuiltin(obj): continue
        if inspect.ismodule(obj): continue
        if inspect.isclass(obj): continue
        if inspect.isfunction(obj): continue
        if inspect.ismethod(obj): continue
        yield obj
</code>

