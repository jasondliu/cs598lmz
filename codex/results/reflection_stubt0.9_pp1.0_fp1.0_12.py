fn = lambda: None
gi = (i for i in ())
fn.__code__ = list(gi)
fn()

del gi, fn

x = "field.name"
try:
    exec(f"{x} = 0", globals(), None)
except ValueError:
    print("OK")

try:
    exec(f"{x} = 0", None, globals())
except ValueError:
    print("OK")

fn = lambda: None
fn.__code__ = len
try:
    fn()
except TypeError:
    print("OK")

del fn

try:
    exec(len, None, None)
except ValueError:
    print("OK")

try:
    exec(len, None, None, None)
except ValueError:
    print("OK")

try:
    exec([], None, None)
except ValueError:
    print("OK")

try:
    exec([], [1, 2, 3], {3: 4, 5: 6})
except TypeError:
    print("OK")

try:
    exec([], {}, {3: 4, 5: 6})
