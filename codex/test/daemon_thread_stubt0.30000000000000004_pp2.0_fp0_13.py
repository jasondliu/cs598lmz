import sys, threading

def run():
    for i in range(10000):
        print(i)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
    print('thread finished')

if __name__ == '__main__':
    main()
