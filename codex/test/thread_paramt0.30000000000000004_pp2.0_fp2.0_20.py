import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello, world!\n")).start()

# 使用内置函数
from time import sleep
threading.Thread(target=lambda: sleep(5)).start()

# 使用参数
threading.Thread(target=lambda: sys.stdout.write("Hello, world!\n"), args=("Hello, world!\n",)).start()

# 使用关键字参数
threading.Thread(target=lambda: sys.stdout.write("Hello, world!\n"), kwargs={"s": "Hello, world!\n"}).start()

# 使用关键字参数和参数
threading.Thread(target=lambda: sys.stdout.write("Hello, world!\n"), args=("Hello, world!\n",), kwargs={"s": "Hello, world!\n"}).start()

# 使用关键字
