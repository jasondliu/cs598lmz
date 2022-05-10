import sys, threading
threading.Thread(target=lambda: sys.stdout.write('foobar\n')).start()
sys.exit()
 
# Output: "foobar" on the next line of the console.
