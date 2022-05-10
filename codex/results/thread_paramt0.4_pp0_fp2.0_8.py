import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello\n")).start()

# 下面的代码是错误的，因为它会引发一个异常
# threading.Thread(target=lambda: sys.stdout.write("Hello\n")).run()

# 下面的代码也是错误的，因为它会引发一个异常
# threading.Thread(target=lambda: sys.stdout.write("Hello\n")).start().run()

# 下面的代码也是错误的，因为它会引发一个异常
# threading.Thread(target=lambda: sys.stdout.write("Hello\n")).start().start()

# 下面的代码也是错误的，因
