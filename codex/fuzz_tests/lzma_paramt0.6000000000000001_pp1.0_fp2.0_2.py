from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self: bytes()

from subprocess import Popen
from subprocess import PIPE

from multiprocessing import Process
from multiprocessing import Queue

from threading import Thread

from time import sleep

from shutil import rmtree

from os import listdir
from os import path
from os import remove
from os import mkdir
from os import walk
from os import devnull

from sys import stdout
from sys import stderr

from json import loads as parseJSON
from json import dumps as stringifyJSON

from traceback import format_exc

from tempfile import TemporaryFile

from lzma import LZMAFile

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM

from struct import pack
from struct import unpack

from base64 import b64decode

from hashlib import sha1

from io import BytesIO

from random import randrange

from select import select

from errno import EAGAIN

from hashlib import sha256

from hmac
