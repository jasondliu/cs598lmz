from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

while True:
    try:
        s.unpack(raw_input())
    except Exception as e:
        print e
        break
```

### 第三题

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

# os.system('cat /flag')

f = open('/flag', 'r')
print f.read()
```

### 第四题

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get

def get_flag():
    url = 'http://127.0.0.1:1337/flag'
    token = 'd8c8b8e9f7c929e9f7f8e9d8'
    headers = {'Authorization': 'Bearer {}'.format(token)}
    r = get(url, headers=headers)
   
