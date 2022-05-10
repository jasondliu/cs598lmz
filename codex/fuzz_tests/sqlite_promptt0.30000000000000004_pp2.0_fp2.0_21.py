import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

libc = ctypes.CDLL(ctypes.util.find_library('c'))

def thread(libc):
    libc.pthread_exit(0)

t = threading.Thread(target=thread, args=(libc,))
t.start()
t.join()

conn = sqlite3.connect(':memory:')
</code>
This code crashes with the following stack trace:
<code>#0  0x00007ffff7b7b9f2 in __GI___libc_free (mem=0x1) at malloc.c:2927
#1  0x00007ffff7b7b9f2 in __GI___libc_free (mem=0x7ffff7dd2a58) at malloc.c:2927
#2  0x00007ffff7b7b9f2 in __GI___libc_free (mem=0x7ffff7dd2a58) at malloc.c:2927
#3  0x00007ffff7b7b9f2 in __GI___libc_free (mem
