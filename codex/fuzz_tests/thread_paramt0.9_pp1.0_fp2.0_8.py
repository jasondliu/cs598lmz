import sys, threading
threading.Thread(target=lambda: os.system('xdg-open "http://localhost:9000/"')).start()
</code>

