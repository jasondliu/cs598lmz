import select
import logging
import os
import subprocess
import sys

try:
    import RPi.GPIO as GPIO
except ImportError:
    print "This program requires Python RPI.GPIO module installed."
    sys.exit(1)

import Adafruit_DHT

log = logging.getLogger('airpi')


class BasePlugin(object):
    """
    All sensor plugins should derive from this class.  Each sensor plugin will
    be passed a settings object which contains settings specific to that
    sensor, along with a generalSettings object which contains general settings
    like time settings.  Many settings objects will provide a location for the
    sensor plugin to write to, this will be in a subdirectory "data" of the
    settings object's output directory.
    """
    def __init__(self, settings=None, generalSettings=None, binary=False, command=None,
                 selectable=False, nonblocking=False, mask=None, encode=None,
                 sensors=None, name=None, unit="", commandName=None,
                 passToOutput=False, shutdown_event=
