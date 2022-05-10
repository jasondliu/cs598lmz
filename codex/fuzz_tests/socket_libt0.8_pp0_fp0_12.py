import socket

from jupyter_client import KernelManager

from ipython_genutils.py3compat import unicode_type
from traitlets import HasTraits, Type, Unicode, Instance, Any, List, Set, cast_unicode
from ipython_genutils.py3compat import string_types
from ipykernel.kernelbase import Kernel
from ipykernel.kernelapp import IPKernelApp
from ipykernel.comm import Comm
from ipykernel.comm import CommManager

from smtplib import SMTP

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import atexit

import threading

from .logger import init_logger

###########
# Logging #
###########

logger = init_logger("jupyter-cron-kernel")

#############
# Constants #
#############

SENDMAIL_PATH = "/usr/sbin/sendmail"

##############
# Decorators #
############
