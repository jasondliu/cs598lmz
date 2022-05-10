from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a)
print(b)
print(a == b)
print(a is b)
print(type(a))
print(type(a) == type(b))
print(type(a) is type(b))
print(isinstance(a, FunctionType))

run = [1,2,3]
for i in run:
    print(i)
for i in iter(run):
    print(i)
print(iter(run))
print(iter(run) == iter(run))
print(iter(run) is iter(run))
print(id(iter(run)) == id(iter(run)))
print(id(iter(run)) is id(iter(run)))

print()

run = {}
for i in run:
    print(i)
for i in iter(run):
    print(i)
print(iter(run))
print(iter(run) == iter(run))
print(iter(run) is iter(run))
print(id(iter(run)) == id(
