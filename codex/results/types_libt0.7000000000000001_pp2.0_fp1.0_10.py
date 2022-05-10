import types
types.MethodType(partial_sq, int)

# Python 2.x
#
# >>> from types import MethodType
# >>> int.partial_sq = MethodType(partial_sq, int)
# >>> int.partial_sq(4)
# 16
# >>> int.partial_sq(5)
# 25
# >>> int.partial_sq(6)
# 36
# >>> int.partial_sq
# <unbound method int.partial_sq>
# >>> int.partial_sq.im_self
# <type 'int'>
# >>> int.partial_sq.im_func
# <function partial_sq at 0x7fba8cef9a28>
# >>> int.partial_sq.im_func.func
# <function sq at 0x7fba8cef9b18>
# >>> int.partial_sq.im_func.args
# (2,)
# >>> int.partial_sq.im_func.keywords
# >>> int.partial_sq.im_func.__dict__
# {'func': <function sq at 0x7fba8
