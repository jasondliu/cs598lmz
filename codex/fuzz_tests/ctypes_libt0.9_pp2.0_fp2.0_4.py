import ctypes
ctypes.__file__
</code>

It might appear on the other hand that if you set the registry keys (as described above) the folder where the custom dll was located suddenly disappears from <code>sys.path</code>. This is the normal behavior. What the registry setting does is only a very naive search. The Python interpreter will search the folder of the custom dll (if there is any) and it will search one folder more. If the module is not found, the search will stop and an exception will pop up. This behavior is also explained in the Microsoft documentation.

