import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import os
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# import cx_Oracle
# import pandas as pd
# import numpy as np
# import datetime
# import time
# import os
# import sys
# import re
# import logging
# import logging.handlers
# import traceback
# import shutil
# import multiprocessing
# import threading
# import subprocess
# import math
# import json
# import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy.types import NVARCHAR, Float, Integer, DateTime, Date
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy import Column, String, Integer, Float, DateTime, Date
# from sqlalchemy import and
