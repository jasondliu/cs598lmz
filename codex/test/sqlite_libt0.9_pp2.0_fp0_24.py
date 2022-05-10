import ctypes
import ctypes.util
import threading
import sqlite3
from sys import exit
import uuid
from subprocess import call
from fcntl import ioctl
from contextlib import contextmanager
from ctypes import (c_uint, c_uint16, c_void_p, c_char_p, c_int, c_char, c_ssize_t, c_size_t,
                    create_string_buffer, sizeof, addressof, Union, POINTER)
from typing import Union
from typing import TypedDict
from pathlib import Path
from modules.logger import logger
from modules.helpers import ConvertBytesToString
from modules.update import CheckUpdates
from tabulate import tabulate
from flask import Flask, render_template, request, redirect, url_for
from flask import send_from_directory

from modules.menu_base import MenuBase
from modules.menu_system_config import MenuSystemConfig
from modules.menu_network import MenuNetwork
from modules.menu_update import MenuUpdate
from modules.menu_status import MenuStatus

# Declare the webapp
app = Flask(__name__)


