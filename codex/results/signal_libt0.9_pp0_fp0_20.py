import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    print("Iniciando")

    try:
        sys.path.append('/home/pi/Desktop/rpi/')
        sys.path.append('/home/pi/Desktop/rpi/sensor_modules/')
        import Config

        config = Config.READ_CONFIG()
        SETTINGS_FILE = config.settings_file
        IP = config.HOME_IP
        PORT = config.PORT

        sys.path.append(
            '/home/pi/Desktop/rpi/sensor_modules/'+ SETTINGS_FILE +'/')

        from time import sleep
        import _thread
        import datetime
        import os
        import platform
        import Cameras


        print("\n")
        print("*************************")
        print("*                       *")
        print("*  Base Camera Uploader *")
        print("*                       *")
        print("*    author:  Aldo Ulises  *")
        print("*                       *
