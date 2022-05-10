import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()
import time

def get_time(time_format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(time_format, time.localtime(time.time()))

def get_str_time(time_format='%Y%m%d%H%M%S'):
    return time.strftime(time_format, time.localtime(time.time()))

def get_str_date(time_format='%Y%m%d'):
    return time.strftime(time_format, time.localtime(time.time()))

def get_date(time_format='%Y-%m-%d'):
    return time.strftime(time_format, time.localtime(time.time()))

def get_date_time(time_format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(time_format, time.localtime(time.time()))
