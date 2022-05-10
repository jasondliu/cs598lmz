import sys, threading
threading.Thread(target=lambda:sys.stdout.write('Hello from a background thread\n')).start()
"""

class Node:
    """
