import threading
# Test threading daemon

def main():
    t = threading.Thread(target=hello)
    t.daemon = True
    t.start()
    time.sleep(0.1)
    print("Main thread")

def hello():
    print("Hello world")

if __name__ == "__main__":
    main()

# Threading:
# import threading
# import time
#
# def worker():
#     print("Thread {} started".format(threading.current_thread().getName()))
#     time.sleep(1)
#     print("Thread {} finished".format(threading.current_thread().getName()))
#
# threads = list()
# for i in range(5):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# print("Program finished")

# Threading:
# import threading
# import time
#
# def worker(arg):
#     print("Thread {} started
