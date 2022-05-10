from types import FunctionType
list(FunctionType(lambda:1))

# [28] 函数的引用计数问题

def fa(x):
    print("a")
    def fb(y):
        print("b")
        def fc(z):
            print("c")
            return x+y+z
        return fc
    return fb

r = fa(1)(2)(3)
print(r)

print(fa.__name__)
print(fa.__doc__)
print(fa.__code__)
print(fa.__closure__)

# [29] 闭包

def fa(x):
    print("a")
    def fb(y):
        print("b")
        def fc(z):
            print("c")
            return x+y+z
        return fc
    return fb

r = fa(1)
print(r)

print(fa.__name__)
print(fa.__doc__)
print(fa.__code__)

