import codecs
codecs.register_error('strict', codecs.ignore_errors)

import ssl
import time
from getpass import getpass, getuser

from er.util import parse_argv, random_password, text_type, trace_context
from er.cmd import Cmd, CmdError
from er.log import init_logger, log_stack
from er.pw import is_valid_passwd
from er.user import User
from er.util import get_readline_buffer, set_parent_file, set_private_ui
from er.xmpp import ConnectionContext


class ShellBrothersContext(object):

  def __init__(self):
    self.connection = None
    self.current_user = None  # current user in the input
    self.history = []
    self.last_user = None     # the last user in the input
    self.new_user = False
    self.reconnect_time = None
    self.scheduled_event = []
    if not get_readline_buffer():
      init_readline()


context = ShellBrothersContext()


