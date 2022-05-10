from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, argdefs=f.__defaults__, closure=f.__closure__))

# The function is called with f(*args, **kwargs)
async def f(*args, **kwargs):
    return await asyncio.sleep(1)

# The function is called with f(**kwargs)
async def f(**kwargs):
    return await asyncio.sleep(1)

# The function is called with f(**kwargs)
async def f(a, b, **kwargs):
    return await asyncio.sleep(1)

# The function is called with f(*args, **kwargs)
async def f(a, *args, b=42, **kwargs):
    return await asyncio.sleep(1)

# The function is called with f(**kwargs)
async def f(a, b=42, **kwargs):
    return await asyncio.sleep(1)

# The function is called with f(*args, **kwargs)
async def f(*
