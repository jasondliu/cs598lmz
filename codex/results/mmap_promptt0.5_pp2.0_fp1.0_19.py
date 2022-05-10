import mmap
# Test mmap.mmap()
import os
import random
import re
import select
import signal
import socket
import string
import subprocess
import sys
import sysconfig
import tempfile
import threading
import time
import unicodedata
import unittest
import uuid
import warnings
import weakref
import zipfile
import zlib
from test import support
from test.support import (
    bigmemtest, bigaddrspacetest, cpython_only, captured_output,
    captured_stdout, cpython_only, findfile, gc_collect, gc_collect_harder,
    gc_collect_generations, gc_disable, gc_enable, gc_isenabled,
    gc_is_tracked, gc_is_tracked_after_finalizer_call, gc_is_tracked_after_finalizer_call_disabled,
    gc_is_tracked_after_finalizer_call_enabled, gc_is_tracked_after_finalizer_call_with_del,
    gc_is_tracked_after_finalizer_
