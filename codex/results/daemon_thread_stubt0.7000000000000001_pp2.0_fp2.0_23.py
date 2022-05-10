import sys, threading

def run():
    i = 0
    while True:
        print(i)
        i += 1
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()

    while True:
        print("main")
        time.sleep(5)

if __name__ == '__main__':
    main()
