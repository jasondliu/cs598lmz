import sys, threading

def run():
    while True:
        print("thread 1")
        time.sleep(1)

def run2():
    while True:
        print("thread 2")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run2)
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()
