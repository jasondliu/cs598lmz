import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
    print("Hello from main")
