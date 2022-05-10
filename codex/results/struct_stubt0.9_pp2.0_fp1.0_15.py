from _struct import Struct
s = Struct.__new__(Struct)
print(s)

"""
Keep in mind that __new__ works with the class, not with the instance. It's called on the class and receives the class as the first argument; it then adds arguments for each of the attributes as per the __init__ method.
"""

"""
The __new__ method has the advantage of being called before the __init__ method. It also has the advantage of being called only when an instance is actually needed, rather than when the class is instantiated. The __new__ method allows the programmer to customize how objects are created but is rarely used in most Python programs.


"""
