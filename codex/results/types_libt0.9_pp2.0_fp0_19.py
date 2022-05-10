import types
types.__doc__
# types.__name__
# types.__module__
class MyClass:
    def __init__(self, my_attr=None):
        self.__dict__["my_attr"] = my_attr
    def __dir__(self):
        return ("my_attr", "my_method")
    def my_method(self):
        return ":P"
    def __getattr__(self, name):
        return "Mmm :V"
    def __setattr__(self, name, value):
        print(f"Setting {name} to {value} !")
        self.__dict__[name] = value

my_obj = MyClass()

# print(dir(my_obj))
# print(my_obj.my_attr)
# print(my_obj.my_method())
# print(my_obj.my_attr)
print(my_obj.my_attr)
my_obj.my_attr = ":)"
print(my_obj.my_attr)

# Good morning friends, I would like
