import threading
# Test threading daemon mode

def worker():
    print('worker')
    t = threading.current_thread()
    # 100_000_000 sec ~ 11 days
    count = 0
    while getattr(t, "do_run", True):
        print('running')
        time.sleep(1)

def main():
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('Stopped')
        #setattr(t, "do_run", False)
    print('Exit')


if __name__ == '__main__':
    main()
