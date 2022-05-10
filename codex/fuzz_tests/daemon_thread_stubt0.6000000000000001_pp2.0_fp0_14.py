import sys, threading

def run():
    try:
        while True:
            print(threading.current_thread().getName(), end='')
            sys.stdout.flush()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt')

if __name__ == '__main__':
    threading.Thread(target=run, name='Thread1', daemon=True).start()
    threading.Thread(target=run, name='Thread2', daemon=True).start()
    threading.Thread(target=run, name='Thread3', daemon=False).start()
    time.sleep(0.5)
