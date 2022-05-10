import socket
import sys
import time
import urllib.request, urllib.parse
from xml.dom import minidom

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

BASE_URL = "http://127.0.0.1:8080/pas/service"
LOGIN_PATH = "/v2/tokens"

TRAIN_PAGE_SIZE = '1000'

TRAIN_PATH = "/v2/knowledge/trainings"
TRAIN_PATH_WITH_ID = "/v2/knowledge/trainings/{0}"
TRAIN_KNOWLEDGE_PATH = "/v2/knowledge/trainings/{0}/knowledge"
TRAIN_KNOWLEDGE_PATH_WITH_ID = "/v2/knowledge/trainings/{0}/knowledge/{1}"
TRAIN_KNOWLEDGE_PATH_WITH_ID_AND_VERSION = "/v2/knowledge/trainings/{0}/knowledge/{1}/{2}"
TRA
