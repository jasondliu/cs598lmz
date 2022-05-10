import selectors
import socket
import types
import time
import threading
from typing import List
from typing import Dict
from typing import Tuple
from typing import Optional

from . import utils

# 这两个常量是消息类型
# 客户端发送给服务器的消息类型
MSG_TYPE_CLIENT_HEART = 'Client Heart'
MSG_TYPE_CLIENT_MESSAGE = 'Client Message'


# 服务器发送给客户端的消息类型
MSG_TYPE_SERVER_HEART = 'Server Heart'
MSG_TYPE_SERVER_MESSAGE = 'Server Message'

# 单播
MSG_TYPE_SINGLE_CAST = 'Single Cast'
MSG_TYPE_SINGLE_CAST_REPLY = 'Single Cast Reply
