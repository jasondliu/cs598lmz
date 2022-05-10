import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import random
import datetime
import time
import json
import re
import logging
import shutil
import traceback
import requests
import subprocess
import threading
import queue
import collections
import urllib.parse
import tempfile

import webbrowser
import html

import praw
import prawcore
import praw.exceptions

import dateutil.parser
import dateutil.tz

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMessageBox
import tkinter.simpledialog as tkSimpleDialog
import tkinter.filedialog as tkFileDialog
import tkinter.colorchooser as tkColorChooser
import tkinter.scrolledtext as tkScrolledText
import tkinter.commondialog as tkCommonDialog
import tkinter.dialog as
