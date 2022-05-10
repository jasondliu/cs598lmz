import ctypes
import ctypes.util
import threading
import sqlite3
import time
import re
import os
import json
import logging
import glob
import psutil
import socket
import tincanchat

### 


def find_chats(chat_path, chat_name):
    if '*' in chat_name:
        chat_name = chat_name.replace('*','.*')
        chat_name = '^%s$' % chat_name

    chat_re = re.compile(chat_name)
    chat_paths = glob.glob(os.path.join(chat_path, '*'))

    chat_paths = [c for c in chat_paths if chat_re.search(c)
                  is not None and os.path.isdir(c)]

    for c in chat_paths:
        logging.info('Found chat %s' % c)

    return chat_paths


class ChatServer(tincanchat.TinCanChat):

    def __init__(self, chat_path='.', chat_name='*'):
        super().__init__()
       
