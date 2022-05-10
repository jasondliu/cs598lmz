import signal
# Test signal.setitimer()

# if you don't know what is setitimer()
# read about it then return here

# setitimer() is simply a timer
# it returns two thing:
# - the elapsed time so far
# - the remaining time
# how?
# it receives 3 arguments:
# - interval
# - elapsed time
# - other
#   - < 0: remaining time
#   - = 0: don't return anything
#   - > 0: return 1, elapsed
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.7)

# return value: (0.0, 0.5)
# 0.5 is the remaining time
# 0.0 is elapsed time

# so now, 0.5 secs have to pass
# before setitimer() returns
# (in other words, I can only call setitimer()
# after 0.5 secs from now)
sleep(0.4)

# now, 0.1 secs have to pass
# before the function returns
signal.setitimer(signal.ITIMER
