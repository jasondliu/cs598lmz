from types import FunctionType
a = (x for x in [1])
print(a)

def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc

def a(x,y):
    return x+y

def b(x,y):
    return x*y

c = partial(a, 1,2)
print(c)

print(c.func)
print(c.args)
print(c.keywords)
print(c())

print(type(c))
print(isinstance(c, FunctionType))

# pickle.dump(a, open("d:/a.txt","wb"))
# pickle.load(open("d:/a.txt","rb"))

print(a.__name__)
print(a.__module__)
print(a
