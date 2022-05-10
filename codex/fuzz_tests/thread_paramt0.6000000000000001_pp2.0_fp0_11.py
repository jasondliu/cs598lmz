import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello\n')).start()
# Hello
threading.Thread(target=lambda: sys.stdout.write('Python\n')).start()
# Python
threading.Thread(target=lambda: sys.stdout.write('World\n')).start()
# World
```

```py
import sys, threading, time

def print_msg(msg):
    time.sleep(1)
    sys.stdout.write(msg + '\n')

threading.Thread(target=print_msg, args=('Hello',)).start()
# Hello
threading.Thread(target=print_msg, args=('Python',)).start()
# Python
threading.Thread(target=print_msg, args=('World',)).start()
# World
```

```py
import sys, threading

def print_msg(msg):
    print(msg)

threading.Thread(target=print_msg, args=('Hello',)).start()
# Hello
threading.Thread(target=print_msg, args
