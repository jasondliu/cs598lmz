import sys, threading

def run():
    while True:
        print("hello world")
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    t.join()

if __name__ == "__main__":
    main()
