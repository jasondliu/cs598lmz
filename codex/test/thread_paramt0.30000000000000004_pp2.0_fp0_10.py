import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 1\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 2\n")).start()

# Thread-local data
# Thread-local data is data whose values are unique to each thread. To manage thread-local data, just create an instance of local (or a subclass) and store attributes on it:

# mydata.py
import threading

local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
