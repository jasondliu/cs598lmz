import sys, threading

def run():
    while True:
        print("Thread 1: still alive")
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()

    while True:
        print("Thread 2: still alive")
        time.sleep(1)

if __name__ == "__main__":
    main()
