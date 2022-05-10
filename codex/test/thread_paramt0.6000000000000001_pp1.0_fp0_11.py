import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Python\n')).start()

# 7.8
# 两个线程，一个输出Hello，另一个输出Python，交替输出
import sys, threading, time
def write(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)
threading.Thread(target=lambda: write('Hello\n')).start()
threading.Thread(target=lambda: write('Python\n')).start()

# 7.9
# 两个线程，一个输出Hello，另一个输出Python，交替输出
import sys, threading, time
