import threading
threading.Thread(target=lambda: None).start()

import time
import random

import pygame

from lib.noop import Noop
from lib.button import Button
from lib.led import Led
from lib.display import Display
from lib.actions import Actions
from lib.events import Events
from lib.alarm import Alarm
from lib.alarmtime import AlarmTime

import logging
logging.basicConfig(level=logging.DEBUG)

class AlarmClock(object):
    def __init__(self):
        self.starttime = time.time()
        self.led = Led()
        self.display = Display()
        self.alarm = Alarm()
        self.alarmtime = AlarmTime()
        self.noop = Noop()
        self.actions = Actions(self.display, self.led, self.alarm)
        self.events = Events(self.actions)
