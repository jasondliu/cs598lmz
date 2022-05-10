import sys, threading

def run():
    try:
        while True:
            print(threading.current_thread().getName())
            sys.stdout.flush()
    except KeyboardInterrupt:
        print('bye')

threading.Thread(target=run).start()
