import sys, threading

def run():
    while True:
        print("Hello World")

threading.Thread(target=run).start()
