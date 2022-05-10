import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2

from datetime import datetime
from datetime import timedelta
from optparse import OptionParser

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pyvirtualdisplay import Display

from pytz import timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy.sql import exists

from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm.exc import NoResultFound

from sqlalchemy.sql import func

from sql
