import ctypes
import ctypes.util
import threading
import sqlite3
import re
import base64

from flask import Flask, render_template, Response, request, g, redirect
from functools import partial
from random import random

from struct import pack, unpack

from OpenSSL import crypto
from OpenSSL.crypto import (
    X509,
    X509Extension,
    X509StoreContext,
    load_certificate_request,
    FILETYPE_PEM,
    FILETYPE_ASN1,
    load_certificate
)

#Constants
NUM_USERS = 200000
NUM_MIDS = NUM_USERS


class Cert(object):
    def __init__(self, uid, mid, pub_key, priv_key):
        self.uid = uid
        self.mid = mid
        self.pub_key = pub_key
        self.priv_key = priv_key


class User(object):
    def __init__(self, email, password, cert):
        self.email = email
        self.password = password
        self.cert = cert


