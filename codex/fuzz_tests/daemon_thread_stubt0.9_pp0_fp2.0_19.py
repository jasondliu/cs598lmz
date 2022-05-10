import sys, threading

def run():
    while True:
        print(os.getcwd())
        time.sleep(5)


def start():
    threading.Thread(target=run).start()
