import sys, threading

def run():
    """
    Test function run in a thread
    """
    for i in range(10):
        time.sleep(0.4)
        print(threading.currentThread().getName() + " " + str(i))

def run_with_join():
    """
    Test function run in two threads, join required
    """
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def run_without_join():
    """
    Test function run in two threads, no join required
    """
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)

    t1.start()
    t2.start()

if __name__ == '__main__':
    print(threading.currentThread().getName() + " started")

    print("Running with join")
    run_with_join()

    print("Running without
