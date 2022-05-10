import ctypes

class S(ctypes.Structure):
    x = None

s = S()
print dir(s)
print s
</code>
output:
<code>['_F_x', '_F_x_lock', '_F_x_offset', '_L_x', '_P_x', '_V_x', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_b_base_', '_b_needsfree_', '_fields_', '_objects', '_objects_', '_subclasshook__', '_x', 'from_param', 'in_dll', 'in_dll_contents', 'in_dll_path', 'in_memory', 'in_memory_contents', 'in_memory_path', '
