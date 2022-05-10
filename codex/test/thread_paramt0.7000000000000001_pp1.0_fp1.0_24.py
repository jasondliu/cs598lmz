import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import os
import time
import json
from picamera import PiCamera
from datetime import datetime
from time import sleep
from azure.storage.blob import BlockBlobService, PublicAccess


