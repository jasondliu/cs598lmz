import threading
# Test threading daemon
class DoWork(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True
    def run(self):
        while(self.running):
            time.sleep(2)
            print("DoWork")
    def stop(self):
        self.running = False

# Class for RaspberryPi LED lighting/blinking
class LED:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.startOff()

    def startOn(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def startOff(self):
        GPIO.output(self.pin, GPIO.LOW)

    def startBlink(self):
        self.blinking = True
        self.blinkThread = BlinkThread(self)
        self.blinkThread.start()

    def stopBlink(self):
        self.blinking = False
       
