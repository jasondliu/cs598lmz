import sys, threading

def run():
    while True:
        print(threading.current_thread().name)
        time.sleep(1)

def main():
    t = threading.Thread(target=run, name='run')
    t.start()
    while True:
        print(threading.current_thread().name)
        time.sleep(1)

