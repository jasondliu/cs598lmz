import threading
threading.stack_size(2 ** 27)

import logging
import logging.handlers

import sys
sys.path.insert(0, '..')
sys.path.insert(0, '../..')

from pytomation.interfaces import Serial, InsteonPLM, InsteonDevice, HAInterface
from pytomation.devices import InterfaceDevice, State, Door
from pytomation.devices import Generic, GenericHADevice
from pytomation.utility.timer import Timer
from pytomation.devices import State

# Show connection details on the console (http://showip.net/)
logger = logging.getLogger('pytomation')
#logger.setLevel(logging.DEBUG)
ghandler = logging.handlers.SysLogHandler('/dev/log', logging.handlers.SysLogHandler.LOG_DAEMON)
f = logging.Formatter('%(name)s: %(levelname)s %(message)s')
ghandler.setFormatter(f)
logger.addHandler(ghandler)

# Define the devices
