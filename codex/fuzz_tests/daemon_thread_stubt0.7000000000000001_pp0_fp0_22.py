import sys, threading

def run():
    commands.getstatusoutput('/home/pi/Desktop/w1thermsensor/w1thermsensor')

thread = threading.Thread(target=run)
thread.start()
</code>

