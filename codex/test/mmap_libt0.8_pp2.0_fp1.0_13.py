import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import yaml

import git

import unittest

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
