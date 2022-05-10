import threading
# Test threading daemon
def run_thread(n):
    print('task', n)
    time.sleep(2)
    print('task done', n, threading.current_thread())

start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run_thread, args=('t-%s' % i,))
    t.setDaemon(True)  # 把当前线程设置为守护线程
    t.start()
    t_objs.append(t)

# for t in t_objs:  # 循环线程实例列表，等待所有线程执行完毕
#     t.join()

print('----------all threads has finished...', threading.current_thread(), threading.active_count())
print('cost:', time.time()
