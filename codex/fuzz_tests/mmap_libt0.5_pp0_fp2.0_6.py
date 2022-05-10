import mmap
import os
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import threading
import time
import traceback
import zipfile
from contextlib import contextmanager
from datetime import datetime
from distutils.version import LooseVersion
from enum import Enum
from functools import wraps
from io import StringIO
from typing import Optional, List, Tuple, Union, Callable, Iterable, Any, Dict
from urllib.parse import urlparse

import attr
import requests
import yaml
from requests.exceptions import ConnectionError

from galaxy.api.errors import NetworkError, BackendNotAvailable, BackendTimeout, InvalidCredentials, UnknownBackendResponse, \
    MissingCredentialsError, ScreenshotDownloadError, NotSupportedByBackend, InvalidToken, MissingGameError, \
    InvalidGameDataError, InvalidGameStatusError, MissingGameStatusError, NoGameDataError, \
    MissingGameDataError, BackendError, RateLimitExceeded, InvalidData, InsufficientPrivileges

from . import __version__
from . import
