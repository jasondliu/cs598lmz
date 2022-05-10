import sys, threading

def run():
    while True:
        print("threading")
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()
    print("main thread")
    time.sleep(1)

if __name__ == '__main__':
    main()
