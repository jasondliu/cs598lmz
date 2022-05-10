import sys, threading

def run():
    i = 0
    while True:
        i += 1
        print(i)

def main():
    print('started main thread')
    print(threading.current_thread())
    t = threading.Thread(target = run, daemon = True)
    t.start()
    print('created secondary thread')
    print(threading.current_thread())
    print('finished main thread')

if __name__ == '__main__':
    main()
