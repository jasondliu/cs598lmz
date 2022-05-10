import select
import sys
import tty
import termios
import time
import math

if len(sys.argv) != 3:
    print "Usage: %s <device> <speed>" % sys.argv[0]
    sys.exit(1)

tty.setraw(sys.stdin)

def read_input(old_settings):
    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        c = sys.stdin.read(1)
        if c == '\x1b':
            break

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def calc_velocity(v):
    return int(round(127.0 * v / 100.0))

def calc_angle(a):
    return int(round(127.0 * a / 180.0))

def set_speed(v):
    v = calc_velocity(v)
    dev.controlWrite(usb.TYPE_CLASS + usb.RECIP_INTERFACE,
