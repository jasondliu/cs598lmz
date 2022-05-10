import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#-------------------------------------------------------------------------------
# Name:        SettingsDialog
# Purpose:     Settings dialog
#
# Author:      Piotr Skalski
#
# Created:     10.03.2013
# Copyright:   (c) Piotr Skalski 2013
# Licence:     GPLv2
#-------------------------------------------------------------------------------

import os
import gtk
import gobject
import pango
import datetime

from copy import copy
from libs.sensors.sensors import Sensors
from libs.sensors.sensor import Sensor
from libs.config import Config
from libs.sensormain import Sensormain
from libs.sensors_model import SensorsModel

# constants

# gconf keys
KEY_SENSORS_DATA_SOURCE = "/apps/sensors/data_source"
KEY_SENSORS_UPDATE_PERIOD = "/apps/sensors/update_period"
