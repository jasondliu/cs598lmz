from types import FunctionType
list(FunctionType(next(iter(vars(FunctionType).values())), globals(), "ans")())

#%%
# 如何判断远程文件是否更新
# 方法：1. get_file_md5()
#       2. get_file_md5()
#       3. 比较文件大小

#%%
# 如何查看当前解释器版本
import sys
print(sys.version)

#%%
# 如何查看当前系统类型
import platform
print(platform.architecture())
print(platform.platform())
print(platform.machine())
print(platform.node())
print(platform.processor())
print(platform.python_version())
print(platform.system())
print(platform.uname())

#%%
# 如何确定
