import sys, threading
threading.Thread(target=lambda: sys.stdout.write('ga\n')).start()
import mod
mod.f()
 
sys.stdout.write('go\n')
sys.stdout.flush()
 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
 
