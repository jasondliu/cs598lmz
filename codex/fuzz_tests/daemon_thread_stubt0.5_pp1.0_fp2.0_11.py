import sys, threading

def run():
    while True:
        sys.stdout.write(".")
        time.sleep(1)

def main():
    threading.Thread(target=run).start()

    while True:
        sys.stdout.write("o")
        time.sleep(1)

if __name__ == "__main__":
    main()
</code>
Running it outputs something like:
<code>oooooooooooooooooooooooooooooooooooooooooooo
............................................
</code>
I.e. the output is broken up into lines. The "." line is the thread, the "o" line is the main thread.
I was expecting the output to be interleaved, like:
<code>oooooooooooooooooooooooooooooooooooooooooooo
.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o
</code>
Why is this? I'm running Python 2.7 on a Ubuntu 12.04 machine.


A:

The Python interpreter is effectively single-threaded.  So, it's not that the threads are
