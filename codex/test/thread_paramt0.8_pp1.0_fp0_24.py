import sys, threading
threading.Thread(target=lambda: __import__('pdb').set_trace()).start()
