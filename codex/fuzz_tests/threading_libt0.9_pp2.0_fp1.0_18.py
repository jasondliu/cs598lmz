import threading
threading.Thread(target=sending_thread).start()
threading.Thread(target=receiving_thread).start()



class PwmSensor(dvbcss.wt.sensors.Sensor):
    """A sensor that is controlled by the value of a PWM signal"""

    def __init__(self, wt, clock, serialPort):
        self.clock = clock
        self.serialPort = serialPort
        
        self.pwmThread = PWMThread(self, wt, clock, serialPort)
        self.pwmThread.start()

    def start(self):
        self.pwmThread.startPolling()
        # print("Starting timer")

    def stop(self):
        self.pwmThread.stopPolling()

    def read(self, clock):
        try:
            return self.pwmThread.read_currentPwm()
        except Exception as e:
            logging.warning("Exception occurred whilst trying to read pwm:" + str(e))
            return None

class PWMThread(dvbcss.util.ClockSyncProt
