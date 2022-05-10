import types
types.MethodType??
# magic function that simplify the definition of a singleton class
class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
 
class MyClass(metaclass=Singleton):
    """
    Example class.
    """

    pass

print(MyClass() is MyClass())
 
 

# The previous implementation works, but if we want to use inheritance, we might need to change the way 
# the super().__call__ is invoked to address the diamond problem (which super to call). As a matter of 
# fact, the implementation in the Python's documentation, uses super(), which correctly calls
