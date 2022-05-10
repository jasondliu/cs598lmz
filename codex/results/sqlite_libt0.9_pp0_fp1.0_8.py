import ctypes
import ctypes.util
import threading
import sqlite3
import json
import btctxstore
import base64
import random
import time
import shutil
import re
import os
import datetime

defaultServers = ['130.211.168.208', '88.99.69.149', '118.69.224.180', '128.199.191.55', '178.62.253.45', '104.244.72.119',
				  '162.243.4.83', '198.199.121.58', '167.114.3.137', '188.166.6.198', '81.169.169.46', '178.62.100.138',
				  '104.131.101.154', '104.236.175.201', '45.32.171.162', '184.73.180.108', '192.241.202.192',
				  '45.79.160.160', '162.243.41.75', '162.243.61.133', '52.78.190.100', '188.166.65.151',
