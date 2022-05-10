import sys, threading

def run():
    print("threading")
    t = threading.Timer(1.0, run)
    t.start()

def main():
    run()
    while True:
        print("main")
        time.sleep(1)

if __name__ == '__main__':
    main()
