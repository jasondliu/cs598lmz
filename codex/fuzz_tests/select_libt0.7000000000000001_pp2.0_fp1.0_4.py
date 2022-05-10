import selectors
import os
import queue
import urllib.request
import sys
import time
import threading
import socket
import sqlite3
import datetime
import hashlib
import json

from pprint import pprint
from bs4 import BeautifulSoup
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse, parse_qs, urljoin

# グローバル変数
# キューのデータサイズ
_QueueSize = 0
# スレッドの最大数
_MaxThread = 0
# 発行されたリクエスト数
_RequestCount = 0
# リクエスト待ちキューに格納された数
_RequestQueueCount = 0
# レスポンス待ちキューに格納された数
_ResponseQueueCount = 0
# クロールしたページ数
_Crawled
