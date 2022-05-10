from types import FunctionType
a = (x for x in [1])
type(a)

# 获取对象信息
# 获得一个对象的所有属性和方法
print(dir('ABC'))

# 如果要获得一个对象的所有属性和方法，可以使用__dict__属性
print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象
