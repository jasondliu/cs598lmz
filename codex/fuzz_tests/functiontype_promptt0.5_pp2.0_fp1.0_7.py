import types
# Test types.FunctionType

def func():
    pass

print(type(func))
print(type(func()) == type(None))

# Test types.LambdaType

lamb = lambda: None

print(type(lamb))
print(type(lamb()) == type(None))

# Test types.GeneratorType

gen = (x for x in range(3))

print(type(gen))
print(type(next(gen)) == type(0))

# Test types.CoroutineType

async def coro():
    await asyncio.sleep(0)

print(type(coro()))

# Test types.AsyncGeneratorType

async def agen():
    yield

print(type(agen()))

# Test types.AsyncIterableType

class AsyncIterable:
    def __aiter__(self):
        pass

print(type(AsyncIterable()))

# Test types.AsyncIteratorType

class AsyncIterator:
    def __aiter__(self):
        return self
    async def
