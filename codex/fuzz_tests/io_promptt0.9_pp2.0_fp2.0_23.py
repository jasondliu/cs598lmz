import io
# Test io.RawIOBase.readinto
import _io
# print(_io.RawIOBase.__doc__)


class RPIO(RPi.GPIO):

    def __init__(self):
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setup(5, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
        RPi.GPIO.add_event_detect(5, RPi.GPIO.FALLING, callback=self.fallback)

    def fallback(self):
        print('Falling Edge')
        ser = serial.Serial(port='/dev/tty/S0', baudrate=9600, timeout=1)
        print(ser.name)
        print(ser.port)
        print(ser.baudrate)
        print('write')
        if ser.inWaiting == 0:
            print('inWaiting0')
        elif ser.inWaiting > 0:
            print('inWaiting>0')
        ser
