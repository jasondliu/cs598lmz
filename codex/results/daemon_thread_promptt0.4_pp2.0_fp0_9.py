import threading
# Test threading daemon
# print("Current Thread:", threading.current_thread().getName())
# print("Is Main Thread:", threading.current_thread().is_alive())
# print("Is Daemon Thread:", threading.current_thread().isDaemon())
# print("Is Daemon Thread:", threading.current_thread().daemon)

# Test threading
# def thread_job():
#     print("This is a thread of %s" % threading.current_thread())
#
# def main():
#     thread = threading.Thread(target=thread_job)
#     thread.start()
#
# if __name__ == '__main__':
#     main()

# Test threading join
# def thread_job():
#     print("T1 start\n")
#     for i in range(10):
#         time.sleep(0.1)
#     print("T1 finish\n")
#
# def T2_job():
#     print("T2 start\n")
#     print("T2 finish\n")
#
#
