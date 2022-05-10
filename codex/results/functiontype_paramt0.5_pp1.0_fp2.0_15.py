from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo"))

# 使用类
class C:
    def __iter__(self):
        return iter([1, 2, 3])

list(C())

# 文件
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

# 生成器
def countdown(n):
    print("Starting to count from", n)
    while n > 0:
        yield n
        n -= 1
    print("Done!")

c = countdown(3)
c
c
c

# 生成器表达式
values = [x / (x - y)
          for x in range(100)
          if x > 50
          for y in range(100)
          if x - y != 0]

values

gen = (x / (x - y)
       for x in range(100)
       if x > 50
       for y in range(100)

