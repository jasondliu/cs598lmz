import sys, threading

def run():
    import time

    while True:
        time.sleep(1)
        print('Hello from thread')

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    print('Hello from main')
    t.join()

</code>
I expect to see the following output:
<code>Hello from main
Hello from thread
Hello from thread
Hello from thread
Hello from thread
Hello from thread
</code>
But instead I get this:
<code>Hello from main
</code>
I'm using a virtualenv with Python 3.8.1 on Debian Buster. I have installed <code>python3-tk</code> and <code>python3-dev</code>.


A:

This is a known bug in the Tkinter module.
https://bugs.python.org/issue36253

