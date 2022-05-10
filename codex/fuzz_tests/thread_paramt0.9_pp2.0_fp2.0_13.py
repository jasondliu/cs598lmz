import sys, threading
threading.Thread(target=lambda: sys.stdout.write('foobar\n')).start()
sys.exit()
 
# Output: "foobar" on the next line of the console.
</code>

All you need to do is work out what thread to join on, and modify the code accordingly.

