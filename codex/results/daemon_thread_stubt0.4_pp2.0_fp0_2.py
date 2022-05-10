import sys, threading

def run():
    while True:
        print("thread")
        time.sleep(0.5)

thread = threading.Thread(target=run)
thread.start()

def main():
    print("main")
    time.sleep(1)

if __name__ == "__main__":
    main()
