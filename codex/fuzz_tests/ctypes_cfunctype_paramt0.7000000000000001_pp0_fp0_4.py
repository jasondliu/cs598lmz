import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float)

@contextmanager
def demo_context(n):
    print("Hello from context")
    yield n
    print("Goodbye from context")

def demo_func(x):
    print("Hello from func")
    return x + 42.0



# Demo I: Function is dynamically typed

x = demo_func
print(x(1))
print(x(1.0))
print(x("hello"))

# Demo II: Function type is fixed at definition time

x = FUNTYPE(demo_func)
print(x(1))
print(x(1.0))
print(x("hello"))


# Demo III: Context manager is dynamically typed

with demo_context(42) as x:
    print(x)

with demo_context("hello") as x:
    print(x)

# Demo IV: Context manager type is fixed at definition time

with CONTEXTTYPE(demo_context)(42) as x:
    print(x)

with CONTEXTTYPE(demo
