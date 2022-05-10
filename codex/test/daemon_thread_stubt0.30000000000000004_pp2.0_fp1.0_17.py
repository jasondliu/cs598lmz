import sys, threading

def run():
    for i in range(5):
        print(i)
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()
    while True:
        print('main')
        time.sleep(1)

