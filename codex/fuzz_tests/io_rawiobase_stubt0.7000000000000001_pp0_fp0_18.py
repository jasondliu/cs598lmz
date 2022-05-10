import io
class File(io.RawIOBase):
    pass

f = File()
print(f)

# __new__ 方法是在类的实例化过程中被调用的特殊方法。
# 它的第一个参数是类本身，而其他参数和通常的方法参数没有区别。
# 当实例化过程被调用时（例如，当你使用 Foo(1, 2) 语句来实例化一个类），
# Python 会依次使用以下步骤来创建对象并返回它：
#
#     1
