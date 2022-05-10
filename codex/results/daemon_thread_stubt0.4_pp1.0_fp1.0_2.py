import sys, threading

def run():
    while True:
        print("Hello")

def main():
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()

if __name__ == "__main__":
    main()
</code>
I am running this code on a Windows machine. When I run this code, it prints "Hello" infinitely.
I want to run this code for a specific time, say, 10 seconds. How can I do this?


A:

<code>import sys, threading, time

def run():
    while True:
        print("Hello")

def main():
    thread = threading.Thread(target=run)
    thread.start()
    time.sleep(10)
    thread.join()

if __name__ == "__main__":
    main()
</code>

