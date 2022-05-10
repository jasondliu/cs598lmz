import signal
signal.signal(signal.SIGALRM, handler)
signal.alarm(2)

def servoPosition(pos):
    pin = 19
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    pwm=GPIO.PWM(pin, 50)
    pwm.start(0)
    pwm.ChangeDutyCycle(pos)
    
def stopMotor():
    GPIO.output(13, 0)
    GPIO.output(16, 1)
    GPIO.output(19, 0)
    GPIO.output(20, 1)
    
def moveForwardMotor():
    GPIO.output(13, 1)
    GPIO.output(16, 0)
    GPIO.output(19, 1)
    GPIO.output(20, 0)
