import sys, threading
threading.Thread(target=lambda:sys.stdout.write(input())).start()
</code>
Not only does this do exactly what you want, but it also appears to be the fastest method!

