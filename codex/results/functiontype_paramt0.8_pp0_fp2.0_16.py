from types import FunctionType
list(FunctionType(f.__code__, globals(), 'my_func').__closure__)
#[<cell at 0x10a1b5868: int object at 0x10a1a49a0>, <cell at 0x10a1b5860: int object at 0x10a1a4a00>]

#最后修改过外部变量后再调用函数一次
nonlocal x
x = 2
f()
#5



#可以使用成员变量
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())
#9 9 9

#使用成员变量但是不要直接引用，而是在函
