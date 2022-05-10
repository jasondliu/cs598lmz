import socket
import signal

import socketserver
import threading

from . import config
from . import const
from . import util
from . import version
from . import xlog
from .connect_control import ConnectControl
from .connect_manager import ConnectManager
from .local_proxy_server import LocalProxyServer
from .pac_proxy_server import PacProxyServer
from .proxy_session import ProxySession
from .task_manager import TaskManager
from .webserver import WebServer
from .user_agent_parser import UserAgentParser
from . import forward_server
from . import detect_ip
from . import simple_http_server

xlog.log_init()

logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=config.user_path + '/xlog.log',
                filemode='w')

console
