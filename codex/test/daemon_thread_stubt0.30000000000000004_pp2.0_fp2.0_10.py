import sys, threading

def run():
    while True:
        print("Hello from thread")
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
