import threading
threading.stack_size(1024*1024*1024)

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
import os

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtNetwork import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import *

from ui.main_window import *
from ui.login_dialog import *
from ui.new_account_dialog import *
from ui.forgot_password_dialog import *
from ui.new_post_dialog import *
from ui.new_comment_dialog import *
from ui.new_group_dialog import *

from u
