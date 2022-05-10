import socket
import time

timeZone = sys.argv[1]

# get the system time
#systemTime = dt.datetime.now(tz.gettz(timeZone))
systemTime = dt.datetime.now()

#configure timezone
os.environ['TZ'] = timeZone
time.tzset()

#get the current timezone time
localTime = dt.datetime.now()

print("The current time for zone " + timeZone + " is: " + localTime.strftime("%H:%M"))
print("The current system time is: " + systemTime.strftime("%H:%M"))

#if the time is between 5pm and midnight, play the night music
if (localTime.hour >= 18) or (localTime.hour <= 23):
    print("It is night time")
    # create an INET, STREAMing socket
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.20', 5000))

