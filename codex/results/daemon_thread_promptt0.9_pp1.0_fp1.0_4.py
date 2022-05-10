import threading
# Test threading daemon mode

def task1():
    print("Start task1")
    time.sleep(3)
    print("End task1")

def task2():
    print("Start task2")
    print("End task2")

def main():
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    # t2.setDaemon(True)
    t1.start()
    t2.start()
    # main thread will wait t1 complete then exit
    t1.join()
    print("All task done")

if __name__ == '__main__':
    main()
