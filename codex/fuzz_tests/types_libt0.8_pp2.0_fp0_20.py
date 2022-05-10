import types
types.FunctionType

def fn(x):
    return 2*x

fn.__name__
fn.__name__ = 'double'
fn.__name__
fn.__doc__
fn.__call__(5)

#if an attribute of an object is a function, it defines a method
#you can bind it to another object
#so that the method will be called when the object is used as a function

l = [1,2,3]
len(l)

def my_len(l):
    return len(l)

l.__len__ = my_len
len(l)

#everything in Python is an object
#everything has methods and attributes
#you can add more of your own

#isinstance
isinstance('a', str)
isinstance(1, int)

#issubclass
issubclass(int, object)
issubclass(int, float)

#type()
type('a')

#dir() to list attributes
dir(1)
dir(int)

#repr() and str()
repr('
