import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Snow'))

>>> threading.Thread(target=lambda: sys.stdout.write('Snow'))
<_MainThread(MainThread, started 8488)>
>>> thread.Thread(target=lambda: sys.stdout.write('Snow'))
<_MainThread(MainThread, started 8488)>
>>> exit()
Use exit() or Ctrl-Z plus Return to exit

>>> sys.stdout.write('Snow')
SnowUse exit() or Ctrl-Z plus Return to exit
>>> 
>>> import sys
>>> exit()
Use exit() or Ctrl-Z plus Return to exit

>>> import threading
>>> sys.stdout.write('Snow')
SnowUse exit() or Ctrl-Z plus Return to exit
>>> 
>>> threading.Thread(target=lambda: sys.stdout.write('Snow'))
<_MainThread(MainThread, started 55572)>
>>> threading.Thread(target=lambda: sys.stdout.write('Snow'))
<_MainThread(MainThread, started 55572)>
>>> 
>>> import sys

