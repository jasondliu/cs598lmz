import ctypes
ctypes.cast(addr_from_name(name), ctypes.POINTER(Mesh))
</code>
I get the error "TypeError: expected LP_Mesh instance instead of pointer instance". 
How can I access the data of the pymel.core.Mesh "mesh" through ctypes.

