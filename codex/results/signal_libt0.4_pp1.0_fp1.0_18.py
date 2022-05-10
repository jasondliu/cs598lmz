import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# Get the current date
today = datetime.datetime.now()

# Get the last date of the previous month
# (i.e. if today is April 2nd, then get March 31st)
last_day_prev_month = calendar.monthrange(today.year, today.month-1)[1]
last_day_prev_month = datetime.date(today.year, today.month-1, last_day_prev_month)

# Get the first date of the current month
# (i.e. if today is April 2nd, then get April 1st)
first_day_cur_month = datetime.date(today.year, today.month, 1)

# Get the last date of the current month
# (i.e. if today is April 2nd, then get April 30th)
last_day_cur_month = calendar.monthrange(today.year, today.month)[1]
last_day_cur_month = datetime.date(today.year
