import signal
# Test signal.setitimer function
# nbr signals received by handler
touch_counter = 0
logger = ""
instr.minit()
instr.setFileLogger(logger, "file_logger")
instr.setCounterLogger(logger, "counter_logger")
instr.setIntervalLogger(logger, "interval_logger")
def handler(signum, frame):
    instr.log(logger, "handler", signum, touch_counter+1)
    touch_counter = touch_counter+1
    if touch_counter >= 2:
        instr.log(logger, "handler", "sleep")
        time.sleep(2)
signal.setitimer(signal.ITIMER_REAL, 1, 0.5)
signal.signal(signal.SIGALRM, handler)
time.sleep(1)
signal.signal(signal.SIGALRM, signal.SIG_IGN)
instr.mend()
instr.displayLog(logger)
 
"""
[out]
file_logger
