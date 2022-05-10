import types
types.ModuleType.__getattribute__ = None
import RPi.GPIO as GPIO             # Import GPIO library


# Define output pins
LEDs = [17, 22, 23, 24, 25]

#Setup GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
for i in LEDs:
  GPIO.setup(i, GPIO.OUT)    # Set as outputs

while True:
  for i in LEDs:
    GPIO.output(i, GPIO.LOW) #Turn off all LEDs
  for i in LEDs:
    GPIO.output(i, GPIO.HIGH) #Turn on single LED
    time.sleep(1)             #Wait for 1 second
