import sys, threading

def run():
    while True:
        a = 1

def main():
    for i in range(0, 2):
        t = threading.Thread(target=run)
        t.start()

if __name__ == "__main__":
    from timeit import Timer
    t = Timer("main()", "from __main__ import main")
    print t.timeit(1)
</code>
On my machine (2.3 GHz, 4GB RAM, Python 2.7.2), I'm getting about 0.4s for 2 threads, and about 0.8s for 4 threads.  I'm assuming that this means it's using both cores correctly.

