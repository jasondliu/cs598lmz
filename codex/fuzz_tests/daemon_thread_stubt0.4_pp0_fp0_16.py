import sys, threading

def run():
    print(threading.current_thread())

def main():
    print(threading.current_thread())
    for i in range(10):
        t = threading.Thread(target=run)
        t.start()

if __name__ == '__main__':
    main()
