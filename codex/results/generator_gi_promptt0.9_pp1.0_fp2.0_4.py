gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code.co_flags & 0x4) # 0x4 == CO_ITERABLE_COROUTINE
# Test iteration over gi
try:
    for i in gi:
        pass
except TypeError:
    pass

# Test gi.gi_running == 1 when suspending
gi = (i for i in range(1, 4))
print(gi.gi_running) # == 0, as iterator is not created yet
next(gi) # create iterator with gi_running == 1
print(gi.gi_running) # == 0
try:
    gi.send(None)
except TypeError:
    pass
print(gi.gi_running) # 1

try:
    gi = (i for i in range(1, 4)).__aiter__()
except TypeError:
    pass
try:
    gi = (i for i in range(1, 4)).__anext__()
except TypeError:
    pass
try:
    gi = (i for i in range(1, 4)).__aenter__()

