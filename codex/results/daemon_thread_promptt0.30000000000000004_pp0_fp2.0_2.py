import threading
# Test threading daemon
from time import sleep

from django.test import TestCase
from django.utils import timezone

from .models import *
from . import tasks
from . import views

# Create your tests here.

class TestThreading(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Thread {} started".format(self.name))
        sleep(1)
        print("Thread {} stopped".format(self.name))

class TestThreadingDaemon(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Thread {} started".format(self.name))
        while True:
            sleep(1)
            print("Thread {} running".format(self.name))

class TestThreadingDaemon2(threading.Thread):
    def __init__(self, name):
        threading.Thread
