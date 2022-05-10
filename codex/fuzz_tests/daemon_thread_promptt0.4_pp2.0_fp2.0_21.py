import threading
# Test threading daemon

def run(n):
    print('task',n)
    time.sleep(2)
    print('task',n,'done')

start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.setDaemon(True)
    t.start()
    t_objs.append(t)

# for t in t_objs:
#     t.join()

print('-----all threads has finished....')
print('cost:',time.time()-start_time)

# import threading
# import time
#
# def run(n):
#     print("task",n)
#     time.sleep(2)
#     print("task done",n,threading.current_thread())
#
# start_time = time.time()
# t_objs = []
# for i in range(50):
#     t = threading.Thread(target=run,args=("t-
