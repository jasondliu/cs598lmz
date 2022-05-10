from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# TypeError: 'function' object is not iterable

# The following is a function that returns a function:
def f():
    def g():
        return 1
    return g

# The following is a function that returns a function that returns a function:
def f():
    def g():
        def h():
            return 1
        return h
    return g

# The following is a function that returns a function that returns a function that returns a function:
def f():
    def g():
        def h():
            def i():
                return 1
            return i
        return h
    return g

# The following is a function that returns a function that returns a function that returns a function that returns a function:
def f():
    def g():
        def h():
            def i():
                def j():
                    return 1
                return j
            return i
        return h
    return g

# The following is a function that returns a function that returns a function that returns a function that returns a function that returns a function:
def
