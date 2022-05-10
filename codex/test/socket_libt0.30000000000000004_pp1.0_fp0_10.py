import socket
import sys
import time
import threading
import os
import datetime
import random
import math
import json
import signal
import subprocess
import re

from threading import Thread
from threading import Timer
from threading import Event
from threading import Lock
from threading import Condition
from threading import Semaphore

from time import sleep
from time import time

from collections import deque
from collections import defaultdict

from Queue import Queue
from Queue import Empty

from sets import Set

from math import sqrt

from random import randint
from random import choice
from random import sample

from os import listdir
from os.path import isfile, join

from datetime import datetime

from signal import signal, SIGINT

from subprocess import Popen, PIPE

from re import findall

# Global variables

# The number of nodes in the system
num_nodes = 0

# The number of nodes that are alive
num_alive_nodes = 0

# The number of nodes that are alive and are not in the process
