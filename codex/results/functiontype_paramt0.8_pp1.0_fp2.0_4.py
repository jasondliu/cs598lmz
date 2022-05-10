from types import FunctionType
list(FunctionType(lambda : True, {}, None, None, None))
#测试属性。两个对象的__slots__属性是否相等
def compare_slots(obj1, obj2):
    obj1_type = type(obj1)
    obj2_type = type(obj2)
    if obj1_type != obj2_type:
        return False
    if hasattr(obj1, "__slots__"):
        if hasattr(obj2, "__slots__"):
            if obj1.__slots__ == obj2.__slots__:
                return True
    return False
compare_slots([], [])

try:
#测试异常
    1/0
except ZeroDivisionError:
    print("error")
#测试交互式执行环境。把模块加载到交互执行引
