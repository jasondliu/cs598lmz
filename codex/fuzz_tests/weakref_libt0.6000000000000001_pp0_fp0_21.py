import weakref
import sys
import os
import time
import subprocess
import struct

from collections import namedtuple

from . import util
from . import _util

from . import _vendor
from . import _vendor.libusb1

from . import _libusb1

from . import backend
from . import backendmanager

from .core import Device
from .core import DeviceHandle
from .core import DeviceList
from .core import DeviceDescriptor
from .core import ConfigDescriptor
from .core import Interface
from .core import InterfaceDescriptor
from .core import EndpointDescriptor
from .core import IsochronousEndpointDescriptor
from .core import Altsetting
from .core import StandardEndpoint
from .core import StandardInterface
from .core import StandardDevice
from .core import StandardDeviceDescriptor
from .core import StandardConfigDescriptor
from .core import StandardInterfaceDescriptor
from .core import StandardEndpointDescriptor
from .core import StandardIsochronousEndpointDescriptor
from .core import StandardAltsetting
from .core import Standard
