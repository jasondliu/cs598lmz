import types
types.ModuleType.__dict__['__getattr__'] = lambda self, name: getattr(self, name)

import os
import sys
import json
import time
import socket
import hashlib
import datetime
import logging
import logging.config
import logging.handlers
import threading
import traceback
import requests
import subprocess

from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response

from flask_cors import CORS

import yaml

from common.utils import Utils
from common.singleton import Singleton
from common.config import Config
from common.logger import Logger
from common.db import DB

from model.t_user import TUser

from model.t_user_role import TUserRole
from model.t_role import TRole
from model.t_role_permission import TRolePermission
from model.t_permission import TPermission

from model.t_user_permission import TUserPermission

from model.t_user_token import TUserToken

from model.
