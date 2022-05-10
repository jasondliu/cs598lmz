import types
types.ModuleType

# 模块名
print(types.ModuleType.__name__)

# 模块所在的包
print(types.ModuleType.__module__)

# 模块的文档注释
print(types.ModuleType.__doc__)


# 动态创建模块
def create_module(name):
    m = types.ModuleType(name)
    m.__file__ = '<%s>' % name
    m.__package__ = name
    return m


m1 = create_module('m1')
print(m1)

# 模块的属性
print(dir(m1))

# 模块的文档注释
print(m1.__doc__)

# 模块所在的文件
print(m1.__file__)

# 模
