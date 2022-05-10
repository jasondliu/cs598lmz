import sys, threading

def run():
    while True:
        
        data = ser.readline().strip()
        print(data)
        
        if data == "1":
            print("Lights on")
            
            GPIO.output(LED_ON, GPIO.LOW)
            GPIO.output(LED_OFF, GPIO.HIGH)
            
            GPIO.output(LIGHT_ON, GPIO.HIGH)
            GPIO.output(LIGHT_OFF, GPIO.LOW)
            
        elif data == "0":
            print("Lights off")
            
            GPIO.output(LED_ON, GPIO.HIGH)
            GPIO.output(LED_OFF, GPIO.LOW)
            
            GPIO.output(LIGHT_ON, GPIO.LOW)
            GPIO.output(LIGHT_OFF, GPIO.HIGH)
            
        else:
            print("Unknown command")
            
def cleanup():
    ser.close()
    GPIO.cleanup()

LED_ON = 22
LED_OFF = 27
LIGHT_ON = 17
LIGHT_OFF = 4

GPIO
