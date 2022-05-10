import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread\n'), name="test1").start()

print "Hello World\n"

# -*- coding: utf-8 -*- 

import sys, threading

b = threading.Thread(target=lambda: sys.stdout.write("\nHello World\n"), name="test2")
b.start()

while b.isAlive():
    sys.stdout.write("Thread\n")
</code>

