import sys, threading

def run():
    print("Thread started")
    for i in range(1, 100):
        print(i)
        time.sleep(0.1)
    print("Thread ended")

def main():
    print("Main started")
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("Main ended")

if __name__ == "__main__":
    main()
