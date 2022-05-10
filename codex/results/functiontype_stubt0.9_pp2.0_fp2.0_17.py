from types import FunctionType
a = (x for x in [1])
b = iter(a)
print(b)
isinstance(a, Iterator)

# 创建生成器
print("==========创建生成器")
def add(n):
    while True:
        try:
            print("开始休眠")
            time.sleep(1)
            print("休眠结束")
            m = yield n
            print("m: ", m)
            n = n + m
        except GeneratorExit:
            print("===> exit")
add = add(3)
add.__next__()
add.send(2)
add.send(5)
add.send(2)
add.send(5)
add.send(10)
print("===========")
