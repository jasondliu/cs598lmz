import sys, threading

def run():
    while True:
        print("hello")
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        print("world")
        time.sleep(1)

if __name__ == "__main__":
    main()
