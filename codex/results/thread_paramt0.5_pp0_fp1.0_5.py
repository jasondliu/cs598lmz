import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a'))

import sys
sys.stdout.write('\a')

import sys, os
sys.stdout.write('\a')
os.system('echo "\a"')

import sys
sys.stdout.write('\a')
sys.stdout.flush()

import sys
print('\a', end='')

import sys
sys.stdout.write('\a')
sys.stdout.flush()

import sys, termios, tty, time
def beep(secs=1):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        sys.stdout.write('\a')
        sys.stdout.flush()
        time.sleep(secs)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

beep(1)

import sys, termios, tty, time

