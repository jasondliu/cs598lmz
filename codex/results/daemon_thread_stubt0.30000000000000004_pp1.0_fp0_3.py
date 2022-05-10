import sys, threading

def run():
    while True:
        print("Thread")

def main():
    print("Main")
    thread = threading.Thread(target=run)
    thread.start()

if __name__ == "__main__":
    main()
</code>
The output is:
<code>Main
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread
Thread

