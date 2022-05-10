import weakref
import logging
import os
import re
import subprocess
import shlex
import sys

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from calibre import prints
from calibre.constants import iswindows, isosx
from calibre.devices.usbms.driver import debug_print
from calibre.devices.usbms.deviceconfig import DeviceConfig
from calibre.devices.usbms.deviceconfig import EXTRA_CUSTOMIZATION
from calibre.devices.usbms.deviceconfig import EXTRA_CUSTOMIZATION_DEFAULT
from calibre.devices.usbms.deviceconfig import SEND_BOOKS_TO_STORAGE_CARD
from calibre.devices.usbms.deviceconfig import SEND_BOOKS_TO_STORAGE_CARD_DEFAULT
from calibre.devices.usbms.deviceconfig import BOOKS_DIR_SORT_POLICY
from calibre.devices.usbms.deviceconfig import BOOKS_DIR_SORT_POLICY_DEFAULT
