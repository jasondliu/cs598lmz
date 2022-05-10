fn = lambda: None
# Test fn.__code__.co_firstlineno
# Test fn.__code__.co_lnotab
def fn():
    pass

# Test fn.__code__.co_cellvars
# Test fn.__code__.co_freevars
def fn(x, y):
    x = 1
    y = 2
    def g():
        nonlocal x
        nonlocal y
        x = 3
        y = 4
        def h():
            nonlocal x
            nonlocal y
            x = 5
            y = 6
            def i():
                nonlocal x
                nonlocal y
                x = 7
                y = 8
                def j():
                    nonlocal x
                    nonlocal y
                    x = 9
                    y = 10
                    def k():
                        nonlocal x
                        nonlocal y
                        x = 11
                        y = 12
                        def l():
                            nonlocal x
                            nonlocal y
                            x = 13
                            y = 14
                            def m():
                                nonlocal x
                                nonlocal y
                                x = 15
                               
