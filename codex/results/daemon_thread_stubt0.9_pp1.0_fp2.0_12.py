import sys, threading

def run():
    for x in range(10000):
        for y in range(10000):
            print x,y

t = threading.Thread(target=run)
t.start()

# the timeit proves it is i/o bound - because of the threading
# As process before the start
# 3.31 sec in 26.42 sec (0.013 MB/sec)
# as process after the start
# 0.040 sec in 0.56 sec (0.064 MB/sec)
</code>

