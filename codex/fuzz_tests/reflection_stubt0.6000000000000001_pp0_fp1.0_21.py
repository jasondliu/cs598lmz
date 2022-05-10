fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

print("\n\n")

def fn():
    raise Exception('No')

try:
    fn()
except Exception as e:
    print(e)

print("\n\n")

def fn():
    return 1

print(fn())

print("\n\n")

def fn():
    return 1

print(fn())

print("\n\n")

def fn():
    return 1

print(fn())

print("\n\n")

def fn():
    return 1

print(fn())

print("\n\n")

def fn():
    return 1

print(fn())

print("\n\n")

def fn():
    return 1

print(fn())

print("\n\n")

def fn():
    return 1

print(fn())

print("\n\n")

def fn():
    return 1

print(fn())

print("\n\n")

def fn():
    return
