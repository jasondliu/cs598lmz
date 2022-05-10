import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()
s = input()
print(s)
</code>
And read from port: 
<code>from serial import Serial
from threading import Thread
from time import sleep
port = 'COM4'
ser = Serial()
ser.port = port

#ser.baudrate = 460800
ser.baudrate = 9600
ser.timeout = 0.1
ser.write_timeout = 0.1
ser.open()

## let's wait a sec before reading

#sleep(3)

def readSerial_thread():
    while True:
        #print 'reading...'
        if ser.in_waiting &gt; 0:
            print ser.readline()

t = Thread(target = readSerial_thread)
t.start()
</code>
But as input() I want to send data to com port (in another thread of course) and read simultaneously from it. 
How can I do this?
Thanks for answers.


A:

Serial port is nothing like standard input. It is a two-way communication which
