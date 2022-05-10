import ctypes
ctypes.cast(0, ctypes.py_object)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import standard python modules
import sys
import threading
import time

# Import python types
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

# Import device utilities
from device.utilities import bitwise, exceptions, logger
from device.utilities.communication.i2c.main import I2C
from device.utilities.communication.i2c.exceptions import I2CError

# Import driver elements
from device.peripherals.modules.atlas_ec import exceptions
from device.peripherals.modules.atlas_ec.driver import AtlasEcoDriver
from device.peripherals.modules.atlas_ec.communicate import AtlasEcoCommunicate
from device.peripherals.modules.atlas_ec.parse import AtlasEcoParse
from device.peripherals.modules.atlas_ec.calibration import AtlasEcoCalibration
from device.peripher
