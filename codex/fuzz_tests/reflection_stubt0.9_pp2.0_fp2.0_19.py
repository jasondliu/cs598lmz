fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(
    0, 0, 0, 0, b'', b'', (), (), (), '', b'', 0, b'')
gi.gi_frame = fn
sys.setrecursionlimit(2000)
try:
    run_gen(gi)
except RecursionError:
    pass

# Engine#150: RecursionError with large stack along with GeneratorExit
try:
    gi = (i for i in range(1000))
    for i in gi:
        if i == 5:
            gi.close()
except RecursionError:
    pass

# Engine#41: Running out of stack space inside a coroutine raises the wrong
# exception type
def await_infinite():
    await await_infinite()
async def c():
    await await_infinite()
async def g():
    try:
        await c()
    except RuntimeError as e:
        assert 'maximum recursion' in str(e)
        # If a RuntimeError, it's a coroutine, not a generator
run_async(
