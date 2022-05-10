import sys, threading

def run():
    while True:
        print("Thread is running")
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    print("Main thread is running")
    time.sleep(5)
    print("Main thread is done")

if __name__ == "__main__":
    main()
