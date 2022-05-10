import sys, threading

def run():
    while True:
        print("running")
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()
    while True:
        input()

