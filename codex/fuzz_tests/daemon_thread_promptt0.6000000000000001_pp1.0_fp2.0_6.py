import threading
# Test threading daemon
def run_thread(n):
    print('task',n)
    time.sleep(2)
    print('task done',n)

start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run_thread,args=('t-%s'%i,))
    t.setDaemon(True) #把当前线程设置为Daemon守护线程
    t.start()
    t_objs.append(t)

# for t in t_objs:
#     t.join()

print("--- %s seconds ---" % (time.time() - start_time))
print('*************All threads have finished!*************')
print('Main threading id:',threading.current_thread().name)

# task t-0
# task t-1
# task t-2
# task t-3
# task t-4
# task t-5
#
