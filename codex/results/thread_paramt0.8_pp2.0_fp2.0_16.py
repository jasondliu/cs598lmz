import sys, threading
threading.Thread(target=lambda:sys.__stdout__.write(input(''))).start()
```

```python
from __future__ import print_function
import sys, threading
threading.Thread(target=lambda:print(sys.stdin.read())).start()
```

#### 2.4.4 屏幕输出

```python
import sys, subprocess
subprocess.Popen('type ' + __file__, stdout=sys.stdout)
```

```python
import __future__
__future__.print_function(open(__file__))
```

```python
import __future__
__future__.print_function(__file__)
```

```python
import __future__
__future__.print_function(chr(105))
```

```python
import __future__
import time
__future__.print_function(time.strftime('%c'))
```

#### 2.4.5 `pickle` 序列化文
