import ctypes
import ctypes.util
import threading
import sqlite3
import traceback

import zmq
import zmq.devices
import zmq.utils.jsonapi as json

from . import __version__

from . import ws_messages as ws
from . import ws_commands as ws_cmd
from . import ws_responses as ws_rsp
from . import ws_events as ws_evt
from . import ws_tasks as ws_tsk
from . import ws_task_control as ws_tsk_ctl
from . import ws_task_status as ws_tsk_st
from . import ws_task_results as ws_tsk_res

import ws_util
import ws_util.ws_logging
import ws_util.ws_zmq
import ws_util.ws_db
import ws_util.ws_thread

#
# Task management thread
#
class TaskThread(ws_util.ws_thread.Thread):
    """
    This thread is started by the web service when a task is started
