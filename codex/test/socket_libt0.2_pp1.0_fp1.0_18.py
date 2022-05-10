import socket
import sys
import os
import time
import threading
import random
import string
import re
import json
import hashlib
import base64
import struct
import logging
import logging.handlers

# 定义日志输出格式
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

# 定义日志输出格式
fmt = logging.Formatter(LOG_FORMAT, DATE_FORMAT)

# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler
