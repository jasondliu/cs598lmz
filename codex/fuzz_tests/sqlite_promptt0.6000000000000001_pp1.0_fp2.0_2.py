import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect('/tmp/test.db')
c = conn.cursor()
c.execute('''CREATE TABLE test(name, age)''')
c.execute('''INSERT INTO test VALUES('Foo', 20)''')
c.execute('''INSERT INTO test VALUES('Bar', 30)''')
c.execute('''SELECT * FROM test''')
print(c.fetchall())
# Test ctypes
libc = ctypes.CDLL(ctypes.util.find_library('c'))
print(libc.getpid())
# Test threading
def foo():
    print('Threading test')
t = threading.Thread(target=foo)
t.start()
t.join()
```

```
$ docker run -it --rm -v /tmp:/tmp -v /lib64:/lib64 -v /lib:/lib -v /usr/lib:/usr/lib -v /usr/lib64:/usr/lib64 -v /usr/lib32:/usr/lib32 -v /usr/lib
