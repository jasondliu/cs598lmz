import bz2
bz2_comp = bz2.BZ2Compressor()
bz2_comp.compress(chosen_buf)
bz2_comp.flush()

-rw-r--r-- 1 root root  272689 Mar 21 13:51 chosen_buf
-rw-r--r-- 1 root root    1572 Mar 21 13:52 init_p.py
-rw-r--r-- 1 root root   24278 Mar 21 13:52 init_p.pyc
-rw-r--r-- 1 root root  783272 Mar 21 13:52 ssss
-rw-r--r-- 1 root root  968473 Mar 21 13:52 ssss.bz2

```

## Recover secret:

```python

from pwn import *
import bz2
bz2_comp = bz2.BZ2Compressor()
bz2_comp.compress(chosen_buf)
bz2_comp.flush()
print (len(bz2_comp.compress(chosen_buf)))
print(len(chosen_
