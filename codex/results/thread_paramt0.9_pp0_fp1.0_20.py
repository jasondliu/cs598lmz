import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world!\n')).start()
</code>
It will print <code>'Hello world!</code>' to the console and never return anything. 

