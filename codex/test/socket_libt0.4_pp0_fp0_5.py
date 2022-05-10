import socket
import struct
import sys
import time

import boto3
import botocore
import click
import requests

from . import __version__, DEFAULT_TIMEOUT, DEFAULT_URL, DEFAULT_REGION
