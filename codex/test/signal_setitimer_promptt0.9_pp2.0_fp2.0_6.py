import signal
# Test signal.setitimer()
class AlarmException(Exception):
    pass
 
def alarmHandler(signum, frame):
    raise AlarmException
 
def nonBlockingRawInput(prompt='', timeout=3):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = raw_input(prompt)
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

stream = ""

port = '/dev/ttyUSB0'
ser = serial.Serial(port, 9600, timeout=120)

while True:
    line = str(ser.readline())
    line = ''.join(line.split())[2:-1]

    stream = line
    #print (stream)
