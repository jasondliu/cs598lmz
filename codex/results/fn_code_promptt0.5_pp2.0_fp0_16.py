fn = lambda: None
# Test fn.__code__.co_nlocals

def f():
    def g():
        def h():
            pass
    def i():
        def j():
            pass
    def k():
        pass

print(f.__code__.co_nlocals)
print(g.__code__.co_nlocals)
print(h.__code__.co_nlocals)
print(i.__code__.co_nlocals)
print(j.__code__.co_nlocals)
print(k.__code__.co_nlocals)

# Test fn.__code__.co_stacksize

def f():
    def g():
        def h():
            pass
    def i():
        def j():
            pass
    def k():
        pass

print(f.__code__.co_stacksize)
print(g.__code__.co_stacksize)
print(h.__code__.co_stacksize)
print(i.__code__.co_stacksize)
print(j
