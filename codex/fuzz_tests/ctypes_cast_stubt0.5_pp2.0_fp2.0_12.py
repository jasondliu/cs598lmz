import ctypes
ctypes.cast(0, ctypes.py_object)

import os
os.environ['PYTHONPATH'].split(os.pathsep)

import sys
sys.path

import site
site.getsitepackages()

import sysconfig
sysconfig.get_paths()
```

## 参考

- [The Python Tutorial — Python 3.7.3 documentation](https://docs.python.org/3/tutorial/index.html)
- [Python 入门指南 — Python 3.7.3 文档](https://docs.python.org/zh-cn/3/tutorial/index.html)
