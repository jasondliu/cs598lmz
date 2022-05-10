import threading
# Test threading daemon
def test_threading_daemon():
    def daemon():
        print('start.')
        time.sleep(2)
        print('End')
    d = threading.Thread(target=daemon, name='daemon')
    d.setDaemon(True) # daemon thread will end when "main thread" ends
    d.start()
    # d.join()
    print('main thread')

# test_threading_daemon()
#===============================================================================

# Thread Local
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_
