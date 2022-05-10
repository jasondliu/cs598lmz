fn = lambda: None
# Test fn.__code__.co_varnames
def f0(a):
    f0.__code__.co_varnames

def f1(a):
    def f1_1():
        f1_1.__code__.co_varnames
    f1_1()

def f2(a):
    def f2_1():
        def f2_2():
            f2_2.__code__.co_varnames
        f2_2()
    f2_1()

def f3(a):
    def f3_1():
        def f3_2():
            def f3_3():
                f3_3.__code__.co_varnames
            f3_3()
        f3_2()
    f3_1()

def f4(a):
    def f4_1():
        def f4_2():
            def f4_3():
                def f4_4():
                    f4_4.__code__.co_varnames
                f4_4()
            f
