import threading
# Test threading daemon
def run_thread(n):
    print("task ", n)
    time.sleep(2)
    print("task done", n, threading.current_thread())
start_time = time.time()
t_objs = []  # 存线程实例
for i in range(50):
    t = threading.Thread(target=run_thread, args=("t-%s" % i,))
    t.setDaemon(True)  # 把当前线程设置为守护线程
    t.start()
    t_objs.append(t)  # 为了不阻塞后面线程的启动，不在这里join，先放到一个列表里
# for t in t_objs:  # 循环线程实
