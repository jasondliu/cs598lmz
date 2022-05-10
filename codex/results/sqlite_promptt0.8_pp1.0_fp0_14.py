import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
def go_all():
    print('a')
    threading.Timer(1.25, go_all).start()
    conn = sqlite3.connect(':memory:')
    print('b')
    c = conn.cursor()
    c.execute('''create table stocks (date text, trans text, symbol text, qty real, price real)''')
    print('c')
    c.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""")
    print('d')
    conn.commit()
    print('e')
    conn.close()
    print('f')

go_all()

print('End')

# Test threading for all
#https://stackoverflow.com/questions/6358105/python-threading-with-sqlite3
</code>
Result:
<code>a
b
c
d
e
f
End
</code>


A:

From the python threading documentation:
<blockquote>

