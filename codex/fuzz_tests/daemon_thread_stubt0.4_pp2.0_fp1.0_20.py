import sys, threading

def run():
    print('run')
    sys.exit(0)

def main():
    print('main')
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print('main done')

if __name__ == '__main__':
    main()
