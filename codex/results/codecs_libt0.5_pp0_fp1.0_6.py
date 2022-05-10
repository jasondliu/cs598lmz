import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import os
import sys
import logging
import traceback
import csv
import json
import pprint
import datetime
import time
import re
import glob
import math
import shutil
import subprocess
import requests
import boto3
import botocore
import numpy as np
import pandas as pd
import pytz
import lxml.etree
import lxml.html
import lxml.html.clean
import html5lib
import pdfminer
import pdfminer.high_level
import pdfminer.layout
import pdfminer.pdfpage
import PyPDF2
import PyPDF2.utils
import PyPDF2.pdf
import PyPDF2.pdf.filters
import PyPDF2.pdf.utils
import PyPDF2.generic
import PyPDF2.generic._name_object
import PyPDF2.generic._object
import PyPDF2.generic._string_object
import PyPDF2.generic._text_string_object
import PyPDF2
