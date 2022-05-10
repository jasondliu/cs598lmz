import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import json
import random
import requests
import datetime
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy import and_, or_, not_
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import desc
from sqlalchemy import exc
from sqlalchemy import event
from sqlalchemy import DDL
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

import config
import util

#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------
class Database:
    def __init__(
