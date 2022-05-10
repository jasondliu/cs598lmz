import sys, threading

def run():
    for i in range(10):
        print("thread:", i)
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("main thread")

if __name__ == "__main__":
    main()
