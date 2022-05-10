import sys, threading

def run():
    for i in range(100000):
        print(i)

def main():
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
