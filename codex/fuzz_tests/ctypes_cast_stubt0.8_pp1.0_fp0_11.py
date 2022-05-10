import ctypes
ctypes.cast(None, ctypes.c_int)

# ctypes.cast(None, ctypes.c_int)
print(sys.platform)
print(platform.version())
print(platform.python_version())
print(platform.python_compiler())
print(platform.python_implementation())
print(platform.python_branch())
print(platform.python_revision())
print(platform.python_build())
print(platform.python_version_tuple())

#
# print(sys.getdefaultencoding())
# print(sys.getfilesystemencoding())

#
# a = list(map(lambda x: x*3, [1, 2, 3, 4]))
# print(a)
#
#
# L = [lambda x: x * i for i in range(5)]
# for i in L:
#     print(i(5))
#
# L = [lambda x, i=i: x * i for i in range(5)]
# for i in L:
#     print(i(5))
#
# L = [
