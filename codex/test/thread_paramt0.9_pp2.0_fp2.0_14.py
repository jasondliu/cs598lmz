import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x07'), daemon=True).start()
import time
minutes = int(input("How many minutes until you"
"would like to be reminded to leave in 5 minutes? "))
def alert():
    if minutes == 0:
        print("Warning! Time to leave!")
    for _ in range(minutes):
        time.sleep(60)
    print("5 Minutes!")
    time.sleep(300)
    print("Time to go!")
alert()
