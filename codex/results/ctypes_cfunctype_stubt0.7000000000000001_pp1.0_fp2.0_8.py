import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('hello world')
    return 'from c'

# 第二个参数是函数指针
lib.bar(8, fun)
lib.bar(1, lambda x: x+9)

# dll 和 so 动态库

# 查看已经安装的扩展包
# import pip
# packages = pip.get_installed_distributions()
# packages_list = sorted(["%s==%s" % (i.key, i.version)
#     for i in packages])
# print(packages_list)
