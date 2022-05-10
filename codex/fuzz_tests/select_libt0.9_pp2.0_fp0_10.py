import select
import os
import signal

from ampy_method import ampy_method
from pyboard_method import pyboard_method
from pyboard_method import PYBOARD_LONG_TIMEOUT
from pyboard_method import sleep_ms
from pyboard_port_method import pyboard_port_method
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.ori_shell_eventloop import DomTermEventLoop
from prompt_toolkit.shortcuts import PromptSession
from prompt_toolkit.token import Token
from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout, Window
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.clipboard import Clipboard
from prompt_toolkit.enums import EditingMode
from prompt_toolkit.formatted_text import PygmentsTokens
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.filters import Always
from prompt_tool
