import sys, threading

def run():
    print("thread started")
    time.sleep(1)
    print("thread ended")

t = threading.Thread(target=run)
t.start()
</code>
I have tried to run this code in 2 ways:

Run the file directly
Run the file in the terminal (python3.7 file.py)

In both cases, the terminal will be blocked until the thread ends.
I would like to know how to run the program in the terminal without blocking it.

