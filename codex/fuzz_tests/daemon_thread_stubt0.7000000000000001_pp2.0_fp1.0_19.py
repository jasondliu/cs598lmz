import sys, threading

def run():
        print("Hello from threading!")

threading.Thread(target=run).start()

print("Hello from main!")
print("Ola a todos!")
