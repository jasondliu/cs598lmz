import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()
</code>
It works fine, but I have to wait for the thread to start and print the dot.
Is there a way to start the thread and continue the execution of the main thread?


A:

You can use a <code>ThreadPoolExecutor</code> to execute your work in a thread in the background:
<code>from concurrent.futures import ThreadPoolExecutor
from time import sleep

def dot():
    sys.stdout.write('.')

with ThreadPoolExecutor(max_workers=1) as tpe:
    tpe.submit(dot)
    sleep(1)
</code>

