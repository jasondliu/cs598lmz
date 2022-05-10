import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
fun()

# @FUNTYPE
# def fun():
#     return "hello"
# fun()

# @FUNTYPE
# def fun():
#     return [1,2,3]
# fun()

# @FUNTYPE
# def fun():
#     return (1,2,3)
# fun()

# @FUNTYPE
# def fun():
#     return {1,2,3}
# fun()

# @FUNTYPE
# def fun():
#     return {1:2, 3:4}
# fun()

# @FUNTYPE
# def fun():
#     return None
# fun()

# @FUNTYPE
# def fun():
#     return True
# fun()

# @FUNTYPE
# def fun():
#     return False
# fun()

# @FUNTYPE
# def fun():
#     return 1 + 2j
# fun()

# @FUNTYPE
# def fun():
#     return b"hello"
# fun()

# @FUNTYPE
# def fun():
#     return
