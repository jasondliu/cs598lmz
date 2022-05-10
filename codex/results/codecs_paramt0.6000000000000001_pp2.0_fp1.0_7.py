import codecs
codecs.register_error('strict', codecs.ignore_errors)

# log
import logging
import logging.config

# config
import configparser

# email
import smtplib
from email.message import EmailMessage

# json
import json

# re
import re

# csv
import csv

# datetime
import datetime

# os
import os

# glob
import glob

# sys
import sys

# BeautifulSoup
from bs4 import BeautifulSoup


def check_file_exists(file_name):
    """
    ファイルが存在するか確認する。

    :param file_name: ファイル名
    :return: True or False
    """
    if os.path.isfile(file_name):
        return True
    else:
        logging.error("File not found: " + file_name)
        return False


def check_directory_exists(directory_name):
    """
    ディレクトリが存在
