import select
# Test select.select() command
# https://docs.python.org/3/library/select.html

import os
import sys
from socket import *
import socket
import time
from threading import Thread
from queue import Queue

from common.tcp_client import Client
from common.tcp_server import Server
from common.tcp_server_async_select import ServerAsyncSelect

from common.tcp_client import Client
from common.tcp_server import Server
from common.tcp_server_async_select import ServerAsyncSelect

from common.tcp_server_async_select import ServerAsyncSelect
from common.tcp_server_async_select import ServerAsyncSelect
from client_server.async_select_chat_client import AsyncSelectChatClient
from client_server.async_select_chat_server import AsyncSelectChatServer
from client_server.async_select_chat_client import AsyncSelectChatClient
from client_server.async_select_chat_server import AsyncSelectChatServer


#-------------------------------------------------------------------------------
# Check if the script is run directly

