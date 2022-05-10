import threading
# Test threading daemon
# def t1_job():
#     print("T1 start\n")
#     for i in range(10):
#         time.sleep(0.1)
#     print("T1 finish\n")
#
# def t2_job():
#     print("T2 start\n")
#     print("T2 finish\n")
#
# def main():
#     added_thread = threading.Thread(target=t1_job, name='T1')
#     thread2 = threading.Thread(target=t2_job, name='T2')
#     added_thread.start()
#     thread2.start()
#     added_thread.join()
#     thread2.join()
#     print("all done\n")
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


