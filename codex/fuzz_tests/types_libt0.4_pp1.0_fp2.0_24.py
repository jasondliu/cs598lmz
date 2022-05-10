import types
types.NoneType

# 下面的代码在 Python 2.x 中是合法的，但在 Python 3.x 中会出现错误
# class MyClass:
#     pass
#
# def test(obj):
#     if isinstance(obj, (MyClass, types.NoneType)):
#         print('ok')
#     else:
#         print('no')
#
# test(None)
# test(MyClass())

# 在 Python 3.x 中，types.NoneType 被移除了，可以使用内置的 NoneType 代替
class MyClass:
    pass

def test(obj):
    if isinstance(obj, (MyClass, type(None))):
        print('ok')
    else:
        print('no')

test(None)
test(MyClass())
