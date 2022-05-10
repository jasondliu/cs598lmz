import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()
</code>
Upload this to your server and access it.
Edit: tested here

