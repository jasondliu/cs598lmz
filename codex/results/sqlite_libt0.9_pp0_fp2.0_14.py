import ctypes
import ctypes.util
import threading
import sqlite3
import requests
import json
from zeroconf import ServiceBroker, Zeroconf, ServiceInfo, IPv4Address, DSNodeServices
from flask import Flask, jsonify, request, send_file, render_template
from logging.handlers import RotatingFileHandler
from logging import Formatter, ERROR, getLogger
from typing import Optional, Union, List
from werkzeug.datastructures import Headers
from os import path, stat, system, mkdir
from sys import executable
from datetime import datetime
from enum import Enum
from socket import socket, inet_ntoa
from logging import exception
from time import localtime, strftime
from netifaces import interfaces, ifaddresses, AF_INET, AF_LINK
from collections import defaultdict

from configuration import config
from media_controllers import MediaController
from media_preview import MediaPreviewer
from version import version

_log = getLogger('service')

class APISocket(Enum):
    """
    The socket types available for the api socket to use
    """
    TCP = 0  # TCP
