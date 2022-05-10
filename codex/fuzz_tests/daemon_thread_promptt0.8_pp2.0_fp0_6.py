import threading
# Test threading daemon thread
def job():
    print('thread name: ', threading.current_thread().name)
    for i in range(10):
        print(i)
    time.sleep(1)
    print('vanish')

# th = threading.Thread(name='job', target=job, daemon=True)
# th.start()

# if __name__ == '__main__':
#     print(threading.active_count())
#     print(threading.enumerate())
#     print(threading.current_thread())

# Test threading lock
# lock = threading.Lock()
# def job1():
#     global A, lock
#     lock.acquire()
#     for i in range(10):
#         A += 1
#         print('job1: ', A)
#     lock.release()

# def job2():
#     global A, lock
#     lock.acquire()
#     for i in range(10):
#         A += 10
#         print('job2: ', A)
#     lock.release()
