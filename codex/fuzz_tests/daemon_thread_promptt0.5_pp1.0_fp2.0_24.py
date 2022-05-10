import threading
# Test threading daemon
# from concurrent.futures import ThreadPoolExecutor

# Test threading
# import threading
# from queue import Queue
# import time


# Test threading daemon

# Test threading
# q = Queue(maxsize=0)
# threads = []
#
# def worker(i):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         do_work(item)
#         q.task_done()
#
# def do_work(item):
#     time.sleep(0.1)
#
# def main():
#     num_worker_threads = 3
#     for i in range(num_worker_threads):
#         t = threading.Thread(target=worker, args=(i,))
#         t.start()
#         threads.append(t)
#
#     for item in source():
#         q.put(item)
#
#     q.join()
#
#     for i in range(num_worker_threads):
#
