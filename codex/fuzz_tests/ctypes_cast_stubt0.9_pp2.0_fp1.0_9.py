import ctypes
ctypes.cast(id(obj_dict), ctypes.py_object).value

{int: object, 8007094931255: &lt;__main__.MyClass object at 0x7f7cb514cb90&gt;}
</code>
But it doesn't work in the case of an object that does not implement a Hashable interface:
<code>mylist = list()
mylist.append('one')

obj_list = MyClass(mylist)

# Fails:
ctypes.cast(id(obj_list), ctypes.py_object).value
</code>
Is there any way to obtain a reference to the initial container object, directly from the <code>MyClass</code> instance?


A:

You cannot do what you're trying to do. 
Most, but not all objects are hashable, which is the condition allowing insertion into a dict. 
For most, but not all objects you can wrap the object into a tuple, which is nearly always hashable, inserting the object into a dict like a value keyed by the tuple. 
So, you can live with the dict, if you put the
