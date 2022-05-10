import sys, threading

def run():
    print("Thread started")
    for i in range(10):
        print(i)
        time.sleep(0.5)
    print("Thread stopped")

def main():
    print("Main started")
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("Main stopped")

if __name__ == "__main__":
    main()
