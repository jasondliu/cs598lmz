from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<i")
s.unpack_from("\x01\x02\x03\x04")
# (1, )
```

### 开关

```python
from bpf import Switch
Switch(True, {3:4}, 2)
# 2
```

```python
from bpf import Switch
Switch(True, {3:4}, 0)
# 4
```

```python
from bpf import Switch
Switch(True, {0:1, 2:3, 4:5}, True)
# 0
```

```python
from bpf import Switch
Switch(True, {2:3}, False)
# None
```

```python
from bpf import Switch
Switch(True, {2:3}, True, default=True)
# 0
```

### 脚本调试

```python
from bpf import Trace
# python some-script.py
# Trace(True)
```

``
