import threading
# Test threading daemon
import time
# Test time module
import schedule
# Test schedule module


__author__ = 'Jakub Pelikan'
__maintainer__ = 'Jakub Pelikan'
__email__ = 'jpelikan@email.cz'
__status__ = 'Testing'
__version__ = '1.0'


def scheduler():
    """
    Add test job to schedule list
    """
    schedule.every(3).seconds.do(job_every_3s)
    schedule.every().day.at("17:00").do(job_every_day_at_1700)
    schedule.every().hour.do(job_every_hour)
    schedule.every().minute.at(":17").do(job_every_minute_at_17)
    schedule.every(10).minutes.do(job_every_10_minutes)
    schedule.every().monday.do(job_every_monday)
    schedule.every().wednesday.at("13:15").do(job_every_wednesday_at_1315)


def job_
