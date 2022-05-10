from types import FunctionType
a = (x for x in [1])
print(a)
print(next(a))
print(next(a))
print(next(a))
async def foo():
    return 1

print(type(foo))
print(isinstance(foo,FunctionType))

import types
a = types.FunctionType(foo,1)
print(a)

fn = type(lambda x: x + 1, (), {"__module__": __name__})
print(fn)
print(fn.__name__)
print(fn.__module__)
print(fn.__qualname__)
print([x+1 for x in [1,2,3,4]])
print(a+1)
print(fn)
import asyncio
tasks = [
        asyncio.ensure_future(foo()),
        asyncio.ensure_future(foo()),
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    rets = task.result()

loop.close()
import
