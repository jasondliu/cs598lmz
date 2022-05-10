from types import FunctionType
list(FunctionType([], [])
class Base:
    @classmethod
    def i_am_class_method(cls):
        print("I am class method, and cls type is", type(cls))
        
    @staticmethod
    def i_am_static_method():
        print("I am static method")
        
    @property
    def i_am_property(self):
        return "Hello"
    
    
class A(Base):
    def i_am_not_class_method(self):
        print("I am not class method, and self type is", type(self))
a = A()
a.i_am_class_method()
a.i_am_not_class_method()
a.i_am_static_method()
A.i_am_class_method()
A.i_am_class_method()
A.i_am_not_class_method()
Base.i_am_property
A.i_am_property
a.i_am_property

__getattribute__(a, "i_am_property")
