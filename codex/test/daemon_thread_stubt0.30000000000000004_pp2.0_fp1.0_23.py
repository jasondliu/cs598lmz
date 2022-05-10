import sys, threading

def run():
    while True:
        x = input()
        print(x)

threading.Thread(target=run).start()

while True:
    print("hi")
