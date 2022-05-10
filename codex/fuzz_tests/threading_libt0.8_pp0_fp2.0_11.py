import threading
threading.stack_size(67108864) # 64MB stack
sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions

def run_thread(thread_num):
  global thread_num_lock
  while True:
    thread_num_lock.acquire()
    thread_num = next_thread_num
    next_thread_num += 1
    thread_num_lock.release()
    if thread_num == total:
      return
    print("thread_num:", thread_num)
    run_schedule(thread_num)

#start = datetime.datetime.now()
#for i in range(total):
#  run_schedule(i)
threads = [threading.Thread(target=run_thread, args=(i,)) for i in range(num_threads)]
for t in threads:
  t.start()
for t in threads:
  t.join()
#end = datetime.datetime.now()
#print (end - start).seconds


#run_schedule()
#run_sche
