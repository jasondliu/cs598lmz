from types import FunctionType
list(FunctionType(FunctionType.__code__,{},None).__closure__)

def test():
    i = 1
    def test0():
        print(i)
    test0()
test()
# i只是闭包包含的普通对象，不收影响，所以是1
# __closure__[0].cell_contents 才有值

def test():
    i = 1
    def test0():
        print(i)
    i = 2
    test0()
test()
# 1

def test():
    i = 1
    def test0():
        print(i)
    test0()
    i = 2
test()
# 2

def test():
    i = 1
    def test0():
        print(i)
    i = 2
    test0()
test()
# 1

def t():
    def t1():
        print(l[0])
    l = [1,2]
   
