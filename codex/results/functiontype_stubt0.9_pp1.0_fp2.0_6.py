from types import FunctionType
a = (x for x in [1])
print(a)
a = iter([1,2,3])
print(a)
'''
List：访问下标，数据有序，可以改变
Tuple：访问下标，数据无序，不能改变
[]代表创建列表，()代表创建元组。list是可以改变的，tuple是不可变的。
生成器
'''
class Iterable(object):
    def __init__(self, *args):
        self.data = [*args]
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        try:
            item = self.data[self.index]
            self.index += 1
        except:
            raise Stop
