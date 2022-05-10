import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 导入数据库配置
from config import *

# 导入数据库操作模块
from db import *

# 导入爬虫模块
from spider import *

# 导入日志模块
from log import *

# 导入邮件模块
from mail import *

# 导入配置模块
from config import *

# 导入时间模块
from datetime import datetime

# 导入线程模块
import threading

# 导入系统模块
import sys

#
