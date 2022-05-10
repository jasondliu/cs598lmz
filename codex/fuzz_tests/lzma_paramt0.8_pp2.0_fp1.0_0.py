from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
```

```python
# -------------------------------------------------------------------------------
# Name:        flag
# Purpose:
#
# Author:      D161764
#
# Created:     04/11/2014
# Copyright:   (c) D161764 2014
# Licence:     <your licence>
# -------------------------------------------------------------------------------

r = []
for i in range(42):
    pop = raw_input()
    r.append(pop)

flag = "CSCG{flag}"

print ' '.join(r)

```

flag is CSCG{e8ea7a8e87aa86c7a887868a858e87e8ea881c7a887868a858e87e8ea8e86c7a887868a858e87e8ea8c86c7a887868a858e87e8ea8c81c7a887868a858e87e8ea8b8e86c7a887868a858e87e8ea8b8c86c
