import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("QQ群聊天记录查询")

# 安装selenium
# pip install selenium
# 安装chromedriver
# https://npm.taobao.org/mirrors/chromedriver/

# 导入selenium模块
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 引用时间模块
import time

# 引用正则表达式模块
import re

# 引用os模块
import os

# 引用csv模块
import csv

# 引用xlwt模块
import xlwt

# 引用xlrd模块
import xlrd

# 引用xlutils
