from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<L')
s.unpack(b'\x00')
```

### ZipFile

```python
from zipfile import ZipFile
z = ZipFile.__new__(ZipFile)
z.__init__('test.zip')
z.extract('test.py')
```

## 文件

### open

```python
open('test.txt', 'r')
```

### chmod

```python
import os
os.chmod('test.txt', 0600)
```

### unlink

```python
import os
os.unlink('test.txt')
```

### rename

```python
import os
os.rename('test.txt', 'test.py')
```

### mkdir

```python
import os
os.mkdir('test')
```

### rmdir

```python
import os
os.rmdir('test')
```

## 网络


