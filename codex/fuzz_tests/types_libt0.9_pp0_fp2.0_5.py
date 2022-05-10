import types
types.MethodType(lambda self: self.c == 'C', o)
o.m()

# and using __get__
types.MethodType(lambda self: self.c == 'C', o.__dict__, o)
o.m()

# how might this work? (doesn't generalize to a binder that works on class objects)
class MethodType(object):
    __init__(f, d, obj):
        # f is a function, d is the __dict__ to bind f to, obj is the "self" argument
        # store f and d as instance attributes
    __call__(obj):
        # obj is the "self" argument, so add it to the call "args" list
        return f(*args)

# get the descriptor protocol to work with classes
# we need a binder that will work on classes
# classes are objects, so we'll make our descriptor an object

# the binder needs to be an object, since we're going to store it in o's __dict__
class MethodType(object):
    def __init__(self, f, c, d):
