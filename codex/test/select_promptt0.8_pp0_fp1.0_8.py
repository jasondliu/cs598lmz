import select
# Test select.select

import sys, time

if sys.platform[:3] == "win":
    def  sleep(secs):
        time.sleep(secs/1000.0)
else:
    sleep = time.sleep

def slower_system_call():
    sleep(0.1)
    
