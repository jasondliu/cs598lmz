import sys, threading

def run():
    while True:
        input()

threading.Thread(target=run).start()

import time, os

try:
    from timeloop import Timeloop

except:
    os.system("pip install timeloop")
    from timeloop import Timeloop


tl = Timeloop()

count = 0
count2 = 0
count3 = 0

try:
    @tl.job(interval=timedelta(seconds=300))
    def sample_job_every_5s():
        global count
        count += 1
        print ("HI")
        print("\n"*100)
        if count == 3:
            tl.stop()

except:
    print ("Error")

while True:
    tl.start()
