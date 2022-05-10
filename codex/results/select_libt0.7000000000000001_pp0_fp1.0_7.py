import select
import tty
import sys

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def key_is_pressed():
    if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
        return True
    return False

def main():
    while 1:
        if key_is_pressed():
            c = getch()
            if c == '\x1b':
                getch()
                c = getch()
                if c == 'A':
                    print ("up")
                elif c == 'B':
                    print ("down")
                elif c == 'C':
                    print ("right")
                elif c == 'D':
                   
