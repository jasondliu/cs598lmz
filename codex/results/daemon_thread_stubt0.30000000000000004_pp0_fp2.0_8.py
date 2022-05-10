import sys, threading

def run():
    while True:
        print('Thread %s is running...' % threading.current_thread().name)
        time.sleep(1)

print('Thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=run, name='LoopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)

# 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',),
