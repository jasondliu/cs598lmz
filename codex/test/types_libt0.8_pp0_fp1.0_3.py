import types
types.MethodType(lambda self: None, None, MyClass)

# ################################################################################################################################

# This is valid Python 2 code but not Python 3

# class MyClass(object):
#     class_var = 1
#
#     def __init__(self):
#         self.instance_var = 2
#
#     @classmethod
#     def class_method(cls):
#         return cls.class_var + MyClass.class_var
#
#     def instance_method(self):
#         return self.instance_var + self.class_var
#
# print(MyClass.class_method())
# print(MyClass.instance_method())

# The first call is OK in both Python 2 and Python 3 because the class method is called on the class.
# The second call is a problem because it is called on the class instead of an instance.
# The problem is in the method's body because the reference to the class variable self.class_var is problematic.

# ################################################################################################################################

# print(range(7))
#
