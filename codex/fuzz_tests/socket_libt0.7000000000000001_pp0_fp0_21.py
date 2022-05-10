import socket, sys, logging, os
from datetime import datetime, timedelta
import time, threading, Queue
import cv2
import numpy as np
import json
import argparse
import zmq
import base64
import sys
import json
import os
import cv2
import numpy as np
import time
from datetime import datetime
import threading
import Queue
import socket
import sys

# # Set up tracker.
# tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
# tracker_type = tracker_types[1]
# tracker = cv2.Tracker_create(tracker_type)

# tracker = cv2.TrackerMedianFlow_create()
# tracker = cv2.TrackerMOSSE_create()
# tracker = cv2.TrackerKCF_create()
# tracker = cv2.TrackerMIL_create()
tracker = cv2.TrackerBoosting_create()
# tracker = c
