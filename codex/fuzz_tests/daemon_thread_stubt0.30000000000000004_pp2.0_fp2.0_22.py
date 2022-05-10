import sys, threading

def run():
    while True:
        print("Hello")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("Goodbye")
</code>
This code will print "Hello" and "Goodbye" infinitely.

