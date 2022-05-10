import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import argparse
import json
import logging
import logging.config
from collections import namedtuple
from datetime import datetime
import requests
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import OperationalError
from sqlalchemy.pool import NullPool

from . import __version__
from . import __author__
from . import __email__
from . import __license__
from . import __copyright__
from . import __url__
from . import __description__
from . import __keywords__
from . import __name__
from . import __classifiers__
from . import __requires__
from . import __packages__
from . import __platforms__
from . import __scripts__
from . import __
