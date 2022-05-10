import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib.request

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from . import config
from . import utils
from . import youtube_dl_utils
from . import youtube_utils
from . import youtube_video_info

# TODO:
# - Add support for downloading multiple videos at once
# - Add support for downloading playlists
# - Add support for downloading channels
# - Add support for downloading videos from a file
# - Add support for downloading videos from a URL
# - Add support for downloading videos from a URL list
# - Add support for downloading videos from a URL file
# - Add support for downloading videos from a URL file list
# - Add support for downloading videos from a URL file directory
# - Add support for downloading videos from
