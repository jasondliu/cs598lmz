import sys, threading

def run():
    while True:
        print(threading.current_thread().name)
        sys.stdout.flush()

def main():
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()

if __name__ == '__main__':
    main()
</code>

