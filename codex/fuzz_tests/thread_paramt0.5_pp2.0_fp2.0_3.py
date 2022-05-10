import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\x07')).start()

#or
import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\a')).start()

#or
import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\7')).start()
</code>

