import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()
sys.stdout.flush()

"""

Another Variant:
import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()
sys.stdout.flush()

#code

#Input:

#Output:

"""
