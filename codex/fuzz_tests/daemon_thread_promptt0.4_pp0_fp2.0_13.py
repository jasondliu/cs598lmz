import threading
# Test threading daemon
# import threading
# import time
#
# def run(n):
#     print("task",n)
#     time.sleep(2)
#
# start_time = time.time()
# t_objs = []
# for i in range(50):
#     t = threading.Thread(target=run,args=("t-%s" %i,))
#     t.setDaemon(True)
#     t.start()
#     t_objs.append(t)
#
# print("----------all threads has finished...",threading.current_thread(),threading.active_count())
# print("cost:",time.time()-start_time)

# import threading
# import time
#
# def run(n):
#     print("task",n)
#     time.sleep(2)
#
# start_time = time.time()
# t_objs = []
# for i in range(50):
#     t = threading.Thread(target=run,args=("t-%s" %i,))
