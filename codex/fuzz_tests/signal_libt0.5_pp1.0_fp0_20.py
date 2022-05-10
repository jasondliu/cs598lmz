import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import re
import subprocess
import webbrowser
import threading
import platform

try:
    import wx
except ImportError:
    raise ImportError,"The wxPython module is required to run this program"

try:
    import psutil
except ImportError:
    raise ImportError,"The psutil module is required to run this program"

try:
    import psutil
except ImportError:
    raise ImportError,"The psutil module is required to run this program"

try:
    import requests
except ImportError:
    raise ImportError,"The requests module is required to run this program"

try:
    from bs4 import BeautifulSoup
except ImportError:
    raise ImportError,"The BeautifulSoup module is required to run this program"

try:
    import pygame
except ImportError:
    raise ImportError,"The pygame module is required to run this program"

try:
    import pygame.midi
except ImportError:
