import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

#Set timer defaults
timer_interval = 1000
stored_interval = timer_interval #in ms
ramp_duration = 60000 #in ms
ramp_start = 0

#Initialize time loggers
time_logger = []
ramp_logger = []

#Create timer
pygame.init()
timer_object = pygame.time.set_timer(pygame.USEREVENT+1, timer_interval) #update BPM every x ms

#Setup serial port
baud = 921600
port = '/dev/ttyAMA0'
serial_port = serial.Serial(port, baud, timeout=0.1)
serial_port.flush()

#Track if it's the first iteration of the for loop
# so we can send a command before the first BPM update
init = 1

#Set up the ramp
ramp_start = time.time() * 1000 #record time ramp starts in ms
ramp_logger.append(timer_interval)

#Main loop
try:
	while True:
		time
