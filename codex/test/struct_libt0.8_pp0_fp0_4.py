import _struct
import time
import traceback
import pygame
from threading import Thread,RLock
import sys

from threading import Thread,RLock

lock = RLock()

def send(msg):
    lock.acquire()

