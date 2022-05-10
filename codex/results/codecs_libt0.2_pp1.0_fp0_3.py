import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 导入数据库模块
import pymysql
pymysql.install_as_MySQLdb()

# 导入配置文件
from config import config_dict

# 导入flask
from flask import Flask

# 导入蓝图
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 导入session扩展
from flask_session import Session

# 导入redis扩展
from redis import StrictRedis

# 导入日志模块
import logging
from logging.handlers import RotatingFileHandler

# 导入过滤器
from app.utils.common import do_index_class

#
