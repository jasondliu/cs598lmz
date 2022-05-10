import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import datetime
import logging
import logging.config
import argparse
import subprocess

from collections import defaultdict
from collections import Counter
from collections import OrderedDict

from pprint import pprint

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import exists

from sqlalchemy.exc import OperationalError

from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from sqlalchemy.orm.attributes import InstrumentedAttribute

from sqlalchemy.ext.hybrid import hybrid_property

from sqlalchemy.ext.hybrid import hybrid_method

