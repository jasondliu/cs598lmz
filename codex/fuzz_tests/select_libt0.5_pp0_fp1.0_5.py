import select
import termios
import tty

from ev3dev.auto import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev.auto import Motor

LEFT_MOTOR = Motor(OUTPUT_B)
RIGHT_MOTOR = Motor(OUTPUT_C)

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def forward():
    LEFT_MOTOR.run_forever(speed_sp=300)
    RIGHT_MOTOR.run_forever(speed_sp=300)


def backward():
    LEFT_MOTOR.run_forever(speed_sp=-300)
    RIGHT_MOTOR.run
