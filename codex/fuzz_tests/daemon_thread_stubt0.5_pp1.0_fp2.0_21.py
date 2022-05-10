import sys, threading

def run():
    for i in range(100):
        print(i)
        time.sleep(0.1)

def main():
    t = threading.Thread(target=run)
    t.start()
    while True:
        pass

if __name__ == '__main__':
    main()
