gi = (i for i in ())
# Test gi.gi_code.co_flags has new flag CO_ITERABLE_COROUTINE
print("TF" if (gi.gi_code.co_flags & inspect.CO_ITERABLE_COROUTINE) else "FF", end=" ")
gi.gi_code.co_flags ^= inspect.CO_ITERABLE_COROUTINE
# Test gi_yieldfrom
print("TF" if hasattr(gi, "gi_yieldfrom") else "FF", end=" ")
# Test gi_frame by testing gi.__await__()
try:
    gi.__await__()
    gi.gi_frame = None
    print("T", end=" ")
except Exception:
    pass
try:
    gi.__await__()
    print("T", end=" ")
except Exception:
    print("F", end=" ")


print()


# CPython3.5+
try:
    async def AS_008():
        await AS_006()

    class AS_009(asyncio.Task):
        pass

    f
