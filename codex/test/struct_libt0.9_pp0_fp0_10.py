import _struct
import termios
import time
import tty

def get_terminal_attrib():
    terminal_fd = sys.stdin.fileno()
    terminal_attributes = termios.tcgetattr(terminal_fd)
    return terminal_attributes

def set_terminal_attribs(attribute_change):
    """Allows you to modify attributes of the port, including baud rate"""
    terminal_fd = sys.stdin.fileno()
    attribute_change[3] = attribute_change[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(terminal_fd, termios.TCSANOW, attribute_change)

def get_charater_from_keyboard():
    """Returns the character pressed on the keyboard"""
    attribute_change = get_terminal_attrib()
    set_terminal_attribs(attribute_change)
    tty.setcbreak(sys.stdin.fileno())
    key_press = sys.stdin.read(1)
