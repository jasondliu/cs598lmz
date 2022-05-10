import sys, threading

def run():
    for i in range(0, 100):
        print(i)
        time.sleep(0.1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    time.sleep(2)
    sys.exit()

if __name__ == '__main__':
    main()
