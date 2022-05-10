import ctypes
import ctypes.util
import threading
import sqlite3
import hashlib
import os
import time
import hmac
import struct
import json
import sys
import calendar
import socket
import platform
import uuid
import secrets
import re

from . import (cbor, cose, cbor2, jws, jose, exceptions, constants, tls,
               utils, tpm, cose_keys, oci_request, oci_response)

class _TPMT_TK_VERIFIED(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("tag", ctypes.c_uint16),
        ("hierarchy", ctypes.c_uint32),
        ("digest", ctypes.c_uint8 * constants.TPM2_DIGEST_SIZE),
    ]

class _TPMT_SIGNATURE(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("sigAlg", ctypes.c_uint16),
        ("signature", ctypes.c_uint8 * constants.TPM2_DIGEST
