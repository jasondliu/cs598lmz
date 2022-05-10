import threading
threading.stack_size(67108864)

from nanpy import (ArduinoApi, SerialManager)
from nanpy import Servo
from time import sleep

connection = SerialManager()
a = ArduinoApi(connection = connection)
servo = Servo(9)

#servo.attach(9)
#servo.write(0)
#sleep(1)
#servo.write(180)
#sleep(1)
#servo.write(90)

def servo_control(servo, angle):
    servo.write(angle)

def servo_on(servo):
    servo.write(180)

def servo_off(servo):
    servo.write(0)

def servo_auto(servo):
    while True:
        servo.write(0)
        sleep(1)
        servo.write(180)
        sleep(1)

def run():
    servo_auto(servo)

run()
