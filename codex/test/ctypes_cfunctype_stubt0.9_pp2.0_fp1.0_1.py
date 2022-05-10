import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

fun.checktype = False
r = fun()
r
# 输出如下
# int(1)

##### 这里要注意不要直接用一个对象进行checktype判断,这个对象必须是基本类型,例如str int等
def __check_dbapi_type(cursor, ret_type):
    value = ret_type()
    try:
        value.checktype()
    except AttributeError:
        raise DBAPIError

class DBAPIError(Exception):
    pass
