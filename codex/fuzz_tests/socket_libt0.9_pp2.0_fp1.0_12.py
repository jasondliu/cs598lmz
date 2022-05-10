import socket
from threading import Thread
from classes.SmartHome import SmartHome
from interfaces import SocketInterface
from interfaces import ArduinoInterface

TEST_MODE = False

def main():
    if(TEST_MODE):
        import unittest
        unittest.main()
    else:
        home = SmartHome()
        
        sock_int = SocketInterface.SocketInterface(home, 3000)
        arduino_int = ArduinoInterface.ArduinoInterface(home, "/dev/ttyACM2", 115200)

        try:
            sockIntThread = Thread(target=sock_int.start)
            arduinoIntThread = Thread(target=arduino_int.start)
            sockIntThread.start()
            arduinoIntThread.start()

            while True:
                pass
        except KeyboardInterrupt:
            sock_int.stop()

if(__name__ == "__main__"): main()
