from types import FunctionType
a = (x for x in [1])
print (type(a))

b = lambda x : x + 1
print (type(b))

print (next(a))

def test(*argv):
    print (type(argv))
    print (argv)
    print (type(argv[0]))
    c = argv[0][1] + argv[0][0]
    return c

print (test([1,2,3,4]))
