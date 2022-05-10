import mmap
# Test mmap.mmap


#import signal
#import termios, os
#if fd <= 0:
#    fd = sys.stdin.fileno()
#
#old = termios.tcgetattr(fd)
#new = termios.tcgetattr(fd)
#new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
#new[6][termios.VMIN] = 1
#new[6][termios.VTIME] = 0
#
#def handler(signal, frame):
#    termios.tcsetattr(fd, termios.TCSAFLUSH, old)
#    sys.stdout.write('\n')
#    sys.stdout.flush()
#
#termios.tcsetattr(fd, termios.TCSANOW, new)
#
#signal.signal(signal.SIGTSTP, handler)
#signal.signal(signal.SIGCONT, handler)
#print "Press enter to exit. (the program will be paused in terminal after that)"
#

