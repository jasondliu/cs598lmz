import types
types.MethodType(func, None, class_name)

# 动态给类添加方法
def set_age(self, age):
    self.age = age

from types import MethodType
class_name.set_age = MethodType(set_age, class_name)
class_name.set_age(25)
class_name.age

# 动态给类添加方法
def set_score(self, score):
    self.score = score

class_name.set_score = set_score
class_name.set_score(100)
class_name.score

# 动态给类添加方法
class_name.set_score = MethodType(set_score, class_name)
class_name.set_score(100)
class_name.score

# 动态给类添加方法
class_name.set_score = MethodType
