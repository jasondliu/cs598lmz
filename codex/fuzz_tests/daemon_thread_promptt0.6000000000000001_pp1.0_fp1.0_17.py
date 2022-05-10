import threading
# Test threading daemon
# def thread_job():
#     print('This is an added Thread, number is %s' % threading.current_thread())
#
# def main():
#     added_thread = threading.Thread(target=thread_job)
#     added_thread.setDaemon(True) # 守护线程，主线程结束后，守护线程也会结束
#     added_thread.start()
#     print(threading.active_count())
#     print(threading.enumerate())
#     print(threading.current_thread())
#     added_thread.join()
#
# if __name__ == '__main__':
#     main()

# Test threading lock
def job1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1', A)
    lock.release()

def job2():
