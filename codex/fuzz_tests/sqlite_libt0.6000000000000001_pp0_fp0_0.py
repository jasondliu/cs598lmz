import ctypes
import ctypes.util
import threading
import sqlite3
import ssl
import os
import random
import time
import sys
import re
import requests
import base64
import hashlib
import json
import platform
import urllib.request

from io import BytesIO
from queue import Queue
from functools import reduce
from urllib.parse import unquote
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1
from dotenv import load_dotenv

load_dotenv()

# IBM Cloud API keys
API_KEY_WATSON_SPEECH_TO_TEXT = os.getenv("API_KEY_WATSON_SPEECH_TO_TEXT")
API_KEY_WATSON_LANGUAGE_TRANSLATOR = os.getenv("API_KEY_WATSON
