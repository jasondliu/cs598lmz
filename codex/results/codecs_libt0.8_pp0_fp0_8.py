import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
from models import *
import io
from nlp import *
import numpy as np
import time
from flask import Flask
from flask import render_template, request

from flask import jsonify
import json
from flask_cors import CORS
import sys
import random
from dbconnection import *
MANUAL_TOPICS=[
    '公司事项',
    '新增资本',
    '重组',
    '投资',
    '资产重组',
    '变更',
    '清算',
    '增资',
    '风控',
    '借款',
    '股权转让',
    '借贷',
    '股东变更',
    '股
