gi = (i for i in ())
# Test gi.gi_code should fail
try:
    gi.gi_code
except AttributeError:
    pass
else:
    raise RuntimeError("test failed")
try:
    gi.send(None)
except TypeError:
    pass
else:
    raise RuntimeError("test failed")


def f():
    items = [1, 2, 3]
    for item in items:
        yield item
    yield items

it = f()
for item in f():
    print(item)

it, items = it.gi_frame.f_lasti, it.gi_frame.f_locals['items']
assert(it == 9)
assert(items == [1, 2, 3])
it, items = it.gi_frame.f_lasti, it.gi_frame.f_locals['items']
assert(it != -1)
assert(items == [1, 2, 3])

try:
    it.__next__()
except StopIteration as e:
    assert(e.value == [1, 2, 3])

def using_send(
