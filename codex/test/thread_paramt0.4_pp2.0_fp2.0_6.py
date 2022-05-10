import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000))))).start()
print('Hello world!')

# 下面的代码会打印出什么？
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world!\n')).start()
print('Hello world!')

# 下面的代码会打印出什么？
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world!\n')).start()
sys.stdout.write('Hello world!\n')

# 下面的代码会打印出什么？
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world!\n')).start()
sys.stdout.write('Hello world!\n')
