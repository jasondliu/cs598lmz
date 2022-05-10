import sys, threading

def run():
    for i in range(10):
        print(i)
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()

    while True:
        print("Main thread")
        time.sleep(1)

if __name__ == "__main__":
    main()
