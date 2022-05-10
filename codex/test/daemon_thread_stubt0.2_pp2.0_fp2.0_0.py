import sys, threading

def run():
    print("Thread started")
    for i in range(10):
        print(i)
        time.sleep(1)
    print("Thread ended")

if __name__ == "__main__":
    print("Main started")
    t = threading.Thread(target=run)
    t.start()
    print("Main ended")
