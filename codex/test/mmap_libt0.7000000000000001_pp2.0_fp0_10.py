import mmap
import os
import pickle
import re
import requests
import shutil
import sys
import tarfile
import tempfile
import time

from io import BytesIO
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from dateutil import parser
from dateutil.relativedelta import relativedelta
from git import Repo
from git.exc import InvalidGitRepositoryError
from nltk.tokenize import sent_tokenize
from pyblake2 import blake2b
from requests_download import download
from tqdm import tqdm
