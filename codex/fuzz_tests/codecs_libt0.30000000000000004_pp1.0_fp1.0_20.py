import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     25.11.2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import sys
import time
import shutil
import datetime
import subprocess
import configparser
import argparse
import logging
import logging.config
import logging.handlers

import requests
import json

import csv

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import re

import sqlite3

import win32com.client

import win32api
import win32con
import win32gui
import win32process

import win32com.client

import win32com.client as
