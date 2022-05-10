import ctypes
ctypes.cast(0, ctypes.py_object)
sys.getrefcount(None)

# 使用ctypes模块访问C函数库
# 导入库
import ctypes
# 加载库
lib = ctypes.cdll.LoadLibrary('./libpycall.so')
# 调用函数
lib.pycall()

# 使用ctypes模块访问C函数库
# 导入库
import ctypes
# 加载库
lib = ctypes.cdll.LoadLibrary('./libpycall.so')
# 调用函数
lib.pycall()

# 使用ctypes模块访问C函数库
# 导入库
import ctypes
# 加载库
lib = ctypes.cdll.LoadLibrary('.
