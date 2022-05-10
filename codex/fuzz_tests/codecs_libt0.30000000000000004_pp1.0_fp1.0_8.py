import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import os
import sys
import time
import datetime
import argparse
import logging
import logging.config
import json
import re
import glob
import csv
import requests
import urllib
import urllib2
import urlparse
import xml.etree.ElementTree as ET
import xmltodict
import pandas as pd
import numpy as np
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR
from sqlalchemy.types import Integer
from sqlalchemy.types import Float
from sqlalchemy.types import DateTime
from sqlalchemy.types import Date
from sqlalchemy.types import Text
from sqlalchemy.types import Boolean
from sqlalchemy.types import Numeric
from sqlalchemy.types import VARCHAR
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.types import JSON
from sqlalchemy.types import ARRAY
from sql
