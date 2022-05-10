import sys, threading

def run():
    # Get the current working directory
    cwd = os.getcwd()

    # Get the current time
    now = datetime.datetime.now()

    # Get the current time in seconds
    now_sec = time.mktime(now.timetuple())

    # Get the current time in milliseconds
    now_ms = now_sec * 1000

    # Get the current time in microseconds
    now_us = now_ms * 1000

    # Get the current time in nanoseconds
    now_ns = now_us * 1000

    # Get the current time in picoseconds
    now_ps = now_ns * 1000

    # Get the current time in femtoseconds
    now_fs = now_ps * 1000

    # Get the current time in attoseconds
    now_as = now_fs * 1000

    # Get the current time in zeptoseconds
    now_zs = now_as * 1000

    # Get the current time in yoctoseconds
    now_ys = now_zs * 1000

    # Get the current time in
