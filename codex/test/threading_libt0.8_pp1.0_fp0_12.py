import threading
threading.Event()

#Define the GPIO pins:
#button
button=3
#LEDs
blue=22
green=27
red=4
#Relays
relay1=17
relay2=14
relay3=15
relay4=18
relay5=23
relay6=24
relay7=25
relay8=8

#the current state the relays are in
relayState=[0,0,0,0,0,0,0,0]

#Define the GPIO pins as inputs/outputs
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(relay1,GPIO.OUT)
GPIO.setup(relay2,GPIO.OUT)
GPIO.setup(relay3,GPIO.OUT)
