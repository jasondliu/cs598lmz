from types import FunctionType
a = (x for x in [1])
b = [1]
# c = []
# for i in b:
#   c.append(i)
d = (1,3,4,5,6)
e = 2,3,4,5
print(type(a) == type(b), '\n', type(a), type(b), type(c), '\n', type(d), type(e))
# print(isinstance(a, FunctionType), isinstance(b, FunctionType), '\n', type(a), type(b), type(c), '\n', type(d), type(e))

# it works \n works
print("abc\nabc\nbac\nabc\nbac")
print("abc\\nabc\\nbac\\nabc\\nbac")
# it doesn't work
print("""abc
abc
abc""")

a = {'three': 3, 'two': 2, 'one': 1}
s = a.keys()
print(s)
print(sorted(a.keys()))

# define method
def product(x, y):

