import sys, threading
threading.Thread(target=lambda:sys.stdout.write(get_ipython().kernel.blobs['my_token'].decode('utf-8'))).start()

