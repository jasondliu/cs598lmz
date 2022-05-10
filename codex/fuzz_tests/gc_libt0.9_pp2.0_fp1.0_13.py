import gc, weakref

from aria.job import Job, JOB_RUNNING, JOB_FINISHED
from aria.asking import get_input, safe_input
from aria.conf import OPTIONS, CHECK_STRING_LABEL
from aria.conf.format import safe_format, make_format_string
from aria.parser import Parser
from aria.util import get_terminal_size, get_signal_name, primitive_types
from aria.progress import ProgressCallback
from aria.logger import LOG_ERROR, LOG_FULL, LOG_INFO, LOG_DEBUG
from aria.logger import get_logger, start_logging, stop_logging
from aria.event import attach_event, detach_event, fire_event
from aria.downloader import DownloadManager, HttpDownloader
from aria.downloader import SingleFileDownloader, MultiFileDownloader

class Application(object):
  
  '''
  The main application class. This class should not be instantiated directly.
  Please use :mod:`aria.Aria` instead.
