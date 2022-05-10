import lzma
lzma

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from openpyxl import load_workbook

from languages import *
from us_address import us_address

from flask import Flask, Response, json, jsonify, redirect, render_template, request
from werkzeug import secure_filename, FileWrapper
from werkzeug.utils import secure_filename

import csv
from cStringIO import StringIO

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


app = Flask(__name__)

# Choose the language
@app.route('/')
def home():
    return render_template('home.html')

# 主题分词
@app.route('/zh/')
def zh():
    return render_template('zh.html')

# 关键词提取
@app.route('/zh/extracting_key
