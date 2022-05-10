import sys, threading

def run():
    while True:
        time.sleep(1)
        print('{}'.format(threading.current_thread().name))

def main():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    while True:
        time.sleep(1)
        print('{}'.format(threading.current_thread().name))

if __name__ == '__main__':
    main()
</code>

