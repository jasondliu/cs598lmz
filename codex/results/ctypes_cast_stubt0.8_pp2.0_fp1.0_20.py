import ctypes
ctypes.cast(x, y)
```

```python
import importlib
mod = importlib.import_module("find_a_package")
```

```python
#这段代码可以给一个模块创建一个别名，以便你使用不含有点的模块名
import socket as sock
s = sock.socket()
```

```python
import sys
sys.path.append('.')
import spam
```

```python
import spam  # spam模块会被定义在一个以spam命名的可见范围内
spam.eggs()  # 调用这个函数
```

```python
import spam as ham
ham.eggs()
```

```python
from spam import *  #
