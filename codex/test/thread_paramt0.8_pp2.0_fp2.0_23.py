import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# Set up pins
#GPIO_TRIGGER = 23
#GPIO_ECHO    = 24



# Set pins as output and input
#GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
#GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo


# Set trigger to False (Low)
#GPIO.output(GPIO_TRIGGER, False)


# Allow module to settle
#time.sleep(0.5)


# Wrapper function
def measure():
    # This function measures a distance

    #GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    #GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()

