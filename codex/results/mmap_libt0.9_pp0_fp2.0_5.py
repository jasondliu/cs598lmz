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

# 檔案內容
filedata = mmap.mmap(open(filename,'rb').fileno(),filesize,None,mmap.ACCESS_READ)

# sqlite函式組
class sqlite:

	# 初始化
	# conn : 資料庫連線物件
	def __init__(self,conn):
		self.conn = conn

	#
