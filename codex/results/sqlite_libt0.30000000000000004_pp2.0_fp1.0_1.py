import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import json
import re
import subprocess
import logging
from logging.handlers import RotatingFileHandler
import traceback
from datetime import datetime
import platform
from collections import OrderedDict
import pkg_resources

from PyQt5 import QtCore, QtGui, QtWidgets

from electrum_axe.i18n import _
from electrum_axe.util import (format_satoshis, format_time, format_satoshis_plain,
                           format_fee_satoshis, format_fee_float, NotEnoughFunds,
                           NoDynamicFeeEstimates, UserCancelled, profiler,
                           InvalidPassword, format_time_until, timestamp_to_datetime,
                           format_satoshis_nofloat, format_fee_satoshis_nofloat,
                           format_fee_unit, format_satoshis_unit,
                           format_fee_satoshis_plain, format_satoshis_plain_nofloat,
                           format_
