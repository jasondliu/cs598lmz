import ctypes
ctypes.cast(id(0), ctypes.py_object).value = 'spam'
print(id(0))
print(id(1))

# 使用模块的__main__属性
# 在这个模块中，可以检查__name__属性，如果是__main__，说明是直接运行的，如果不是，说明是被别的模块调用的
if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')

# 在模块中测试代码
# 可以在模块中编写
