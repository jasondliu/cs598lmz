import threading
threading.stack_size(1024*1024)

# Initialize the GPIO Pins
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

# Setup LED Pins
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(FAN_PIN, GPIO.OUT)

# Setup button pins
GPIO.setup(FAN_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button to GPIO23
GPIO.setup(LIGHT_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RED_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GREEN_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BLUE
