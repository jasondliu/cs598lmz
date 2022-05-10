import sys, threading

def run():
    print("Thread {} started".format(threading.current_thread().name))
    time.sleep(1)
    print("Thread {} finished".format(threading.current_thread().name))

def main():
    print("Thread {} started".format(threading.current_thread().name))
    for i in range(5):
        t = threading.Thread(target=run, name="thread-{}".format(i))
        t.start()
    print("Thread {} finished".format(threading.current_thread().name))

if __name__ == "__main__":
    sys.exit(main())

# threading.Thread(target=run, name="thread-1").start()
# threading.Thread(target=run, name="thread-2").start()
# threading.Thread(target=run, name="thread-3").start()
# threading.Thread(target=run, name="thread-4").start()
