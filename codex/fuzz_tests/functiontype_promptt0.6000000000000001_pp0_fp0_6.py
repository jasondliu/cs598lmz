import types
# Test types.FunctionType
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test instance
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# Test attr
print(hasattr(obj, 'x'))
print(getattr(obj, 'y', 404))
print(setattr(obj, 'z', 19))
print(getattr(obj, 'z'))

# Test json
import json
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
def student2dict
