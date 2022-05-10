import threading
threading.stack_size(67108864)

import time
import os

import psutil

# import routes
import routes.middleware
import web

# import controller
import controller.controllers

# import model
from model.config import configs
from model.db import db

# import api
from api.v1 import apiv1

# import app
from app.project import project
from app.admin import admin
from app.registry import registry

# 如果是linux系统，需要添加下面两行代码
if os.name == 'posix':
    import resource
    resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, -1))

def set_session():
    """
    Set session
    """
    web.config.session_parameters['cookie_name'] = 'ss_id'
    web.config.session_parameters['cookie_domain'] = None
    web.config.session_param
