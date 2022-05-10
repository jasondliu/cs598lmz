import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        co2.send_co2_1min_avg_cmd()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
handler()

#python /home/pi/forestgarden/ForestGarden.py 

co2 = CO2Meter('/dev/CO2_Serial', 9600)


print "Welcome to CO2Meter.com"
print ""

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

# script for co2meter interfacing with modbus https://github.com/rory/co2meter-modbus.git

try:
    while delays:
        print(co2.read_co2_1min_avg(), end='\r')
        time.sleep(1)
        
finally:
    print ''
    co2.close()
