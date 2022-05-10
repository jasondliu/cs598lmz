import ctypes
ctypes.cast(0, ctypes.py_object).value

# 利用上面的方法，我们可以随意改变 None 的值
import sys
ctypes.cast(id(None), ctypes.py_object).value = 'Spam'
print(None)

# 如果你尝试修改 None 的值，那么在多数情况下程序会立刻崩溃，因为这个值被大量的使用。
# 当然，你可以修改 None 的值，但是你应该清楚你在做什么，并且是否有更好的选择
