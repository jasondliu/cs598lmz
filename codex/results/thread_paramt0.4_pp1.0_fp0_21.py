import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

#
# import threading
#
# def first_function():
#     print("Hello from a thread!")
#
# if __name__ == "__main__":
#     # create a thread
#     t = threading.Thread(target=first_function)
#     # start the thread
#     t.start()
#
#
# import threading
#
# def first_function():
#     print("Hello from a thread!")
#
# def second_function():
#     print("Hello from another thread!")
#
# if __name__ == "__main__":
#     # create a thread
#     t1 = threading.Thread(target=first_function)
#     # create another thread
#     t2 = threading.Thread(target=second_function)
#     # start the threads
#     t1.start()
#     t2.
