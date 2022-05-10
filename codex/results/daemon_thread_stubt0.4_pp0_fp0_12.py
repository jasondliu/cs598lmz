import sys, threading

def run():
    for i in range(20):
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
    for i in range(20):
        print("main", i)
        time.sleep(1)
