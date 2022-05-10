from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>16si')
s.unpack(buf)
# (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 0)
```

比如数据库的查询操作，可以这样使用

```python
from _sqlite3 import Cursor
c = Cursor.__new__(Cursor)
c.__init__(db)
c.execute('SELECT * FROM sample')
c.fetchall()
```

但是这种方式很多时候是不好使的，因为类可能只能使用类方法创建实例。

```python
from datetime import datetime
datetime.now
