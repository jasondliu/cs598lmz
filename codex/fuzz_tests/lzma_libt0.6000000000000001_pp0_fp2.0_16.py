import lzma
lzma.open

import sys
import os
import struct

from struct import pack, unpack

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.factory import ClientDecoder
from pymodbus.transaction import ModbusRtuFramer

import time
import math

from logging.handlers import RotatingFileHandler
import logging

from sys import platform as _platform

import datetime

import sqlite3

import json

import threading

#import subprocess

import paho.mqtt.client as mqtt

import socket

import urllib.request

import time

import serial.tools.list_ports

import requests

import queue

import re

import hashlib

import hmac

import base64

import pyautogui

import win32api

import win32con

import pyper
