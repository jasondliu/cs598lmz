from types import FunctionType
a = (x for x in [1])  # <generator object <genexpr> at 0x7fdaaad5e840>
type(a)
b = {'x':x for x in [1]}
type(b) #<class 'dict'>

d = {1:1}
d.__sizeof__()
d.__sizeof__() + sys.getsizeof(d)

# 协程
import asyncio
@asyncio.coroutine
def hello():
    print("hello1")
    r = yield from asyncio.sleep(1)
    print("hello2")
    return 'test'

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
