gi = (i for i in ())
# Test gi.gi_code.co_flags = CO_GENERATOR | CO_ITERABLE_COROUTINE (0x100100)
print("gi.gi_code.co_flags = ", gi.gi_code.co_flags)
for i in gi:
    pass

# Test __aiter__
class A:
    def __init__(self, a):
        self.a = a
    def __aiter__(self):
        return self
    async def __anext__(self):
        if self.a <= 0:
            raise StopAsyncIteration
        self.a -= 1
        return self.a

ai = A(3)
print("ai.__aiter__().a = ", ai.__aiter__().a)
async def f(ai):
    async for i in ai:
        print(i)

asyncio.run(f(ai))

# Test __anext__
class A:
    def __init__(self, a):
        self.a = a
    async def __anext__(self):
        if
