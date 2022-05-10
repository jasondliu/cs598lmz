import mmap
import datetime
import os
import re
import os.path
import shutil
import json
import sys
from subprocess import call
from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from werkzeug.utils import escape
from blender_server import blender
from crfsuite import predict, train, tag, load_model
from pathlib import Path
from zipfile import ZipFile
from io import BytesIO, StringIO
from boto3.session import Session
from boto3.dynamodb.conditions import Key, Attr
from boto3 import client
from botocore.client import Config
import boto3
import boto
from boto.s3.bucket import Bucket
from boto.s3.key import Key
from boto.s3.connection import S3Connection

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['TRAIN_FOLDER
