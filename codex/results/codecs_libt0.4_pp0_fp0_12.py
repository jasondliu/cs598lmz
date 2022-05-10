import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 导入数据库模块
import pymysql

# 导入Flask模块
from flask import Flask, request, render_template, redirect, url_for, session, flash

# 导入自定义的登录验证装饰器
from utils.login_required import login_required

# 导入自定义的时间转换模块
from utils.time_format import time_format

# 导入自定义的分页模块
from utils.paging import iPagination

# 导入自定义的分页模块
from utils.paging import iPag
