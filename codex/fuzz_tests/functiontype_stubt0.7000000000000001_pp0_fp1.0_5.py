from types import FunctionType
a = (x for x in [1])
print(a)
if isinstance(a,str):
    print("yes")
if isinstance(a,FunctionType):
    print("no")
if isinstance(a,GeneratorType):
    print("yes")

a = [1,2,3]
a[0] = 2
print(a)

a = (1,2,3)
a[0] = 3
print(a)

s = "hello"
s = s.replace("h","a")
print(s)

a = [1,2,3]
b = a
b[0] = 2
print(a)
print(b)

a = (1,2,3)
b = a
b[0] = 2
print(a)
print(b)

a = [1,2,3]
def test(a):
    a[0] = 2
test(a)
print(a)

a = (1,2,3)
def test(a):
    a[0] = 2
test(a)
print(a
