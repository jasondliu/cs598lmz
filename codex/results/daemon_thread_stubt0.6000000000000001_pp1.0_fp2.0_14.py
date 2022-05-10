import sys, threading

def run():
    os.chdir("/home/pi/Desktop/sensor")
    os.system("python3 /home/pi/Desktop/sensor/main.py")
    sys.exit()

threading.Thread(target=run).start()
