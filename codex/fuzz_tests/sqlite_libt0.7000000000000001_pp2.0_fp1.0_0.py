import ctypes
import ctypes.util
import threading
import sqlite3
import time

import _pigpio

# This module provides access to the GPIO on a Raspberry Pi.

# Author: Dave Hylands, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#
# This library provides the basic functions to access the gpio on the
# Raspberry Pi.
#
# To use this library you must first run the pigpiod daemon.
#
# The default port for the socket connection is 8888.
