import lzma
lzma.open = lzma.LZMAFile

import os
import zipfile
import tarfile
import gzip
import shutil
import inspect
import sys
import re
import json
import glob
import subprocess
import multiprocessing
import tempfile
from urllib.parse import urlparse
from urllib.request import urlretrieve
from functools import partial
from tqdm import tqdm
