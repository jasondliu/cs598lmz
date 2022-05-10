import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import config
import urllib
import urllib2
import base64
import json
import sys
import os
import logging
import logging.handlers

from datetime import datetime, timedelta

logger = logging.getLogger('sms-notify')
handler = logging.handlers.SysLogHandler(address = '/dev/log')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def check_schedule():
    now = datetime.now()
    current_hour = now.hour
    current_wday = now.weekday()

    if current_wday in config.schedule and current_hour in config.schedule[current_wday]:
        return True
    else:
        return False

def send_sms(phone, message):
    if not check_schedule():
        logger.debug('Schedule is off')
        return

    logger.info('Sending SMS to %s' % phone)
