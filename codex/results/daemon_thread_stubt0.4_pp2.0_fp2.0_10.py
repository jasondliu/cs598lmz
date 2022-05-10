import sys, threading

def run():
    while True:
        print("Child thread running")
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()

    while True:
        print("Main thread running")
        time.sleep(1)

if __name__ == "__main__":
    main()
</code>
The output is:
<code>Child thread running
Main thread running
Child thread running
Main thread running
Child thread running
Main thread running
Child thread running
Main thread running
Child thread running
Main thread running
Child thread running
Main thread running
Child thread running
Main thread running
Child thread running
Main thread running
</code>
The threads are running in parallel.

