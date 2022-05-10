fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

print("Testing generator code object that emits code")

def rungen(gen):
    try:
        while True:
            gen.send(None)
    except StopIteration:
        pass

def test_gen(gen):
    try:
        rungen(gen)
    except:
        print("Error caught")

def test_func(func):
    try:
        func()
    except:
        print("Error caught")

def gen(limit):
    try:
        while True:
            fn = yield
            fn()
    except StopIteration:
        pass

def create_nested_fn(fn, depth):
    for i in range(depth):
        fn = lambda: fn
    return fn

def code_from_gen(gen, depth):
    for i in range(depth):
        fn = lambda: gen.send(None)
        fn = create_nested_fn(fn, depth)
        gen.send(fn)
    return gen.gi_code

def gen_from_code(code
