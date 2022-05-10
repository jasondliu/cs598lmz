import sys, threading

def run():
    global counter
    for i in range(1000000):
        counter += 1

def main():
    global counter
    counter = 0
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(counter)

if __name__ == '__main__':
    main()
