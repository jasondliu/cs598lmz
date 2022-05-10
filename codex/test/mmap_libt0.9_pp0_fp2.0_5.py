import mmap
import sys
import sqlite3
import os
import subprocess
import re
import datetime
import xml.etree.ElementTree as ET
import shutil
import uuid
import bz2
import json
import opencc

# 要轉換的檔案
filename = './index.dat'
# 轉換過後的檔案
dbname   = '/tmp/index.tmp.db'
# 檔案大小
filesize = os.stat(filename).st_size

