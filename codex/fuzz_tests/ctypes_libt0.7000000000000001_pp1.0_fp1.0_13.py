import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Pokemon Go Bot")

from discord_webhook import DiscordWebhook, DiscordEmbed

from pgoapi import PGoApi
from pgoapi.utilities import f2i, get_cellid
from pgoapi import utilities as util
from pgoapi.exceptions import AuthException, NotLoggedInException, ServerBusyOrOfflineException
from pgoapi.hash_server import HashServer
from pgoapi.location import distance_in_meters, get_neighbors
from pgoapi import protos
from google.protobuf.internal import encoder
from geopy.geocoders import GoogleV3
from s2sphere import CellId, LatLng
from time import sleep
from random import randint
from datetime import datetime
import os
import sys
import struct
import shutil
import logging
import argparse
import threading
import re
import json
import subprocess
import glob
import math
import sqlite3
import requests
import configparser
import base64
import random
import string
import time
import json
