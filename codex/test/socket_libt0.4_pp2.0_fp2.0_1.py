import socket
import sys
import time
import os
import threading
import subprocess
import signal
import logging
import re
import json
import glob
import shutil

import netifaces
import requests
import wget

from subprocess import Popen, PIPE

from pprint import pprint

from flask import Flask, request, redirect, url_for, send_from_directory, render_template, jsonify, Response
from flask_cors import CORS
from werkzeug.utils import secure_filename

from flask_socketio import SocketIO, emit

from . import config

from . import utils

from . import camera

from . import video

from . import audio

from . import video_streamer

from . import video_streamer_2

from . import audio_streamer

from . import video_streamer_3

from . import video_streamer_4

from . import video_streamer_5

from . import video_streamer_6

from . import video_streamer_7

from . import video_streamer
