import ctypes
ctypes.CDLL('/usr/lib/libwiringPi.so', mode=ctypes.RTLD_GLOBAL)

import wiringpi
import time

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO)


# ...

io.pinMode(1,io.PWM_OUTPUT)
io.pinMode(2,io.PWM_OUTPUT)
io.pwmSetMode(io.PWM_MODE_MS)
io.pwmSetClock(192)
io.pwmSetRange(2000)

while True:
	for dc in range(0,101,5):
		io.pwmWrite(1,dc)
		time.sleep(0.1)
	for dc in range(100,-1,-5):
		io.pwmWrite(1,dc)
		time.sleep(0.1)
    
    
# ...
```
