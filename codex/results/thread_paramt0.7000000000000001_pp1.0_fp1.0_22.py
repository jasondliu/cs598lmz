import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\a')).start()
sys.exit(0)
</code>

