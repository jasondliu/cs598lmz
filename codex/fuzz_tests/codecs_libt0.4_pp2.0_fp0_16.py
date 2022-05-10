import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import datetime
import math
import logging
import logging.config
import traceback
import threading

from flask import Flask, request, jsonify, render_template, g, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import desc
from sqlalchemy import and_, or_

from flask_cors import CORS
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_session import Session
from flask_socketio import SocketIO
from flask_socketio import send, emit

from sqlalchemy.exc
