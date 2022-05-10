import signal
signal.signal(signal.SIGHUP,signal.SIG_IGN)
def app_path():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))


import time
from util.parseXml import parseXml
from util.httpUtil import httpUtil
from util.mqttUtil import mqttUtil
from util.session_manage import session_manage
from util.dbUtil import dbUtil
import logging
from util.logUtil import logUtil
from util.threadingUtil import threadingUtil
from util.configobj import configobj
from util.popupUtil import popupUtil
from util.sqliteUtil import sqliteUtil
from util.mailUtil import mailUtil
from util.threadingUtil import my_sched
from util.send_monkey_log import send_monkey_log
from util.check_gui
