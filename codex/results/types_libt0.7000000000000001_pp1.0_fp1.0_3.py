import types
types.MethodType(lambda self, amount: self.value + amount,
                 money_instance, money_class)

# __getattribute__ is called everytime an attribute is accessed
class LostProperty:
    def __getattribute__(self, name):
        return 'huh... {}?'.format(name)

# __setattr__ and __delattr__ control attribute setting and deletion
class ProtectAndHideX:
    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return ~self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        else:
            self.__x = x

    x = property(get_x, set_x)

# __eq__ and __ne__ control equality testing
# __lt__, __le__, __gt__, __ge__ control comparison
class LessThan:
    def __init__(self, n):
        self.n = n

    def __lt__(self, other):
        print('__lt
