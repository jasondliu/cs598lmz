import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
   print("hey")
a = fun()
a()

# c_void_p = POINTER(c_void)   # void*
# functype = CFUNCTYPE(c_void_p)
# dll = cdll.LoadLibrary('..\Bin\DLLTest.dll')
# #dll.add.restype = c_void_p
# add_fun = dll.add
# res = add_fun()
# print(type(res))
# print(res)
# print(add_fun())


# class Bag_Iter:
#     def __init__(self, _obj):
#         self._index = 0
#         self._obj = _obj
#     def __iter__(self):
#         return Bag_Iter(_obj)
#     def __next__(self):
#         if self._index == self._obj.size():
#             raise StopIteration()
#         else:
#             self._index += 1
#             return self._obj.get(self._index - 1)

# class Bag:
#
