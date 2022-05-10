import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 引入数据库配置
from config import *

# 引入数据库操作类
from db import *

# 引入日志操作类
from log import *

# 引入爬虫类
from spider import *

# 引入爬虫类
from utils import *

# 引入爬虫类
from config import *

# 引入爬虫类
from config import *

# 引入爬虫类
from config import *

# 引入爬虫类
from config import *

# 引入爬虫类

