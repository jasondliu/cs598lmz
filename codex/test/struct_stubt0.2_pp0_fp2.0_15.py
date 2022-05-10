from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method (special-cased so you needn't declare it as such) that takes the class of which an instance was requested as its first argument. The remaining arguments are those passed to the object constructor expression (the call to the class). The return value of __new__() should be the new object instance (usually an instance of its class).

# If __new__() does not return an instance of cls, then the new instance's __init__() method will not be invoked.

# __new__() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation.

# __init__() is the most commonly used method. It is called after the instance has been created (by __new__()), but before it is returned to the caller. The arguments are those passed to the class constructor expression. If a base class has an __init__() method, the derived class's __init__() method, if any, must explicitly call it to
