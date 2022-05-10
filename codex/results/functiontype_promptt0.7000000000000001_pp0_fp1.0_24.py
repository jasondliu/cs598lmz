import types
# Test types.FunctionType
print(type(abs)==types.FunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type(x for x in range(10))==types.GeneratorType)

# Test isinstance()
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))
# Test dir()
print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

print(hasattr(obj, 'x')) # 有属性'x'吗？
print(obj.x)
print(hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个
