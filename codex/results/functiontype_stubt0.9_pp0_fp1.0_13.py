from types import FunctionType
a = (x for x in [1])
print(type(a))
b = ( (x for x in [1]) for x in [1,2] )
print(type(b))
print(dir(b))
#c = (x for x in a)
#d = (x for x in (a,b))


#You can set values of the generator, by defing __set__ method
#look at https://www.programiz.com/python-programming/property
# https://julien.danjou.info/python-property-caching/
# https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work
class PropertyCache(object):
    def __init__(self,func):
        print("__init__")
        self.func = func

    def __get__(self, instance, cls):
        print("__get__")
        if instance is None:
            return self
        value = self.func(instance)
        #something, for example set the calculated value to instance.__dict__, 
        #a
