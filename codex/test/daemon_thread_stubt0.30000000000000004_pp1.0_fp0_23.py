import sys, threading

def run():
    while True:
        print('Hello World')
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()
    while True:
        print('Hello Python')
        time.sleep(1)

