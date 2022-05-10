import sys, threading
threading.Thread(target=lambda: sys.stdin.readlines()).start()
sys.stdout.write ( str ( sum ( int ( line ) for line in sys.stdin.readlines() ) ) + "\n" )
