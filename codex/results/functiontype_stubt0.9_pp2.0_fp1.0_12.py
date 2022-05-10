from types import FunctionType
a = (x for x in [1]) # iterator
print(a)
print(type(a))

print()

b = (x for x in range(5))
print(b)
print(type(b))

print()

fn = lambda x: x + 2
print(fn(2))
print(type(fn))

print()

# y = 3
c = lambda x, y=3: print("x is " + str(x) + ", y is", y)
print(type(c))

print()

print("when the function is called, this is the calc")
c(1)
print("")

print("when the function is called, this is the calc")
c(1, 4)
print("")

print("when the function is called, this is the calc")
c(1, y = 4)
print("")

print("when the function is called, this is the calc")
c(1, y = 6)
print("")

print("when the function is called, this is the calc")
c(1, y = 7)
print("")


