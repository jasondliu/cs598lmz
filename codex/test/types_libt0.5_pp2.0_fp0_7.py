import types
types.MethodType(lambda self, *args: None, None, None)

# This is a known issue with Python 3.7
# https://bugs.python.org/issue33891
# We can't do anything about this warning, so disable it.
import warnings
warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>")

import pymysql
import os
import sys
import json
import subprocess
import datetime

import logging
import logging.handlers

import time

import traceback

import requests

import threading

import smtplib
import email.mime.text

import copy

import pprint

import math

import urllib.parse

import re

import ssl

import socket

import hashlib

import argparse

import configparser

import urllib3

import base64

import random

import string

import secrets

import tempfile

import shutil

import pkg_resources

import zlib

import b
