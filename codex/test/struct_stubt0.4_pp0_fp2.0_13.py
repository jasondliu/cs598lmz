from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i")
s.size

# __new__ is called to create a new instance of the class.
# __init__ is called to initialize the instance.
# __new__ is called to create the instance, and then __init__ is called to initialize it.
# __new__ returns the instance, and __init__ initializes it.

# __new__ is called when you create a new instance.
# __init__ is called when the instance is ready to be initialized.
# __new__ is called before __init__, and is responsible for returning a new instance of your class.
# In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.

# __new__ is called when you create a new instance.
# __init__ is called when the instance is ready to be initialized.
# __new__ is called before __init__, and is responsible for returning a new instance of your class.
# In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.


# __new__ is
