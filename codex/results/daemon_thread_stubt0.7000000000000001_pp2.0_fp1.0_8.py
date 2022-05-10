import sys, threading

def run():
    while True:
        print("Hello World")
        time.sleep(1)

def run2():
    while True:
        print("Hello World2")
        time.sleep(1)

def main(argv):
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")

if __name__ == '__main__':
    main(sys.argv)
