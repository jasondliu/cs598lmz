import types
# Test types.FunctionType
def f():
    pass

print(type(f))
# Test types.LambdaType
g = lambda x: x
print(type(g))
# Test types.GeneratorType
def count(n):
    while n > 0:
        yield n
        n -= 1

h = count(5)
print(type(h))
# Test types.CoroutineType
async def hello():
    await asyncio.sleep(1)
    print("Hello world!")

i = hello()
print(type(i))
# Test types.AsyncGeneratorType
async def as_count(n):
    while n > 0:
        yield n
        n -= 1

j = as_count(5)
print(type(j))
# Test types.ClassType
class C:
    pass

print(type(C))
# Test types.TypeType
# NOTE: TypeType is not available in Python 3
#print(type(type))
