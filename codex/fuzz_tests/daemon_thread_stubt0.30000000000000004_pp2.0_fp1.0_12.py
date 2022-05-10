import sys, threading

def run():
    while True:
        print("thread")

def main():
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        print("main")

if __name__ == "__main__":
    main()
