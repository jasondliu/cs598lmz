import ctypes
ctypes.cast(0, ctypes.py_object)

# 检查代码是否符合PEP8标准
# pip install pycodestyle
# pycodestyle --first example_code.py

# Pylint是一个检查代码的工具
# pip install pylint
# pylint example_code.py


# 2. python编译器

# 检查代码编写是否有错误
# python -m py_compile example_code.py
# 编译成.pyc格式
# python -m compileall example_code.py


# 3. 分析器

# 检查代码运行时间
# python -m timeit '"-".join(str(n) for n in range(100))'
# 100000 loops, best of 3: 3.78 use
