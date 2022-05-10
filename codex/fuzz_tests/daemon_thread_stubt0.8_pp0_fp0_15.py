import sys, threading

def run():
    for x in range(0, 100):
        print x
        time.sleep(0.1)

def test():
    for x in range(0, 100):
        print x
        time.sleep(0.1)


if __name__ == "__main__":


    t1 = threading.Thread(target=run)
    t1.daemon = True
    t1.start()

    t2 = threading.Thread(target=test)
    t2.daemon = True
    t2.start()
