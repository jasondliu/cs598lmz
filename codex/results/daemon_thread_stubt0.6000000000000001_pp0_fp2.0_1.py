import sys, threading

def run():
    while True:
        with open('/home/pi/logs/monitor.log', 'a') as f:
            f.write(str(datetime.datetime.now()) + '\n')
        time.sleep(5)

def start():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()

start()

#cron tab command
# */5 * * * * /usr/bin/python /home/pi/monitor.py
# This will run the file every 5 minutes
