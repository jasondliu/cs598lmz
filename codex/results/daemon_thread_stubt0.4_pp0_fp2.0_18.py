import sys, threading

def run():
    print("Thread: ", threading.current_thread().name)
    for i in range(10):
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    print("Main: ", threading.current_thread().name)
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("Main: ", threading.current_thread().name)
