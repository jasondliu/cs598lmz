import ctypes
ctypes.cast(id(objectName), ctypes.py_object).value = [0,1,2]

print(objectName[0:10])

</code>
I get this error:
<code>AttributeError: 'numpy.ndarray' object has no attribute '__array_interface__'
</code>
Is there any way to cast a numpy array or is this impossible?


A:

It's not impossible, but <code>numpy</code>'s arrays store the data somewhere else than the <code>numpy.ndarray</code> object you're referencing, so this is what's causing the <code>AttributeError</code>.
First of, it's not possible for you to use <code>ctypes</code> to cast <code>id(objectName)</code> to a pointer to a list, since <code>id</code> returns an <code>int</code> and not a pointer to a list.
In this situation, maybe the best way to modify your <code>numpy</code> array is to use the <code>numpy.ctypeslib</code> module. The way <
