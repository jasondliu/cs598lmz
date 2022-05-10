import signal
# Test signal.setitimer()
print('Default:', signal.getitimer(signal.ITIMER_PROF))


# def set_timer():
#     signal.setitimer(signal.ITIMER_PROF, 1)
#
#
# signal.signal(signal.SIGPROF, set_timer)
#
#
# # 在测试脚本中不需要右键执行，如何触发呢？
# class Test(unittest.TestCase):

# time.sleep(3)  # 虽然使用了SIGPROF信号，但是不会被触发
import time
import threading
import functools

from kazoo.client import KazooClient

from dao.events_dao import EventsDao
from zk.service_actions import ServiceActions
from zk.registry_tools import RegistryTools
from service.observer import Observer
