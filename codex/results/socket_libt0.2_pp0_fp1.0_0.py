import socket
import sys
import threading
import time
import traceback

import pytest

import pymongo
from pymongo import common
from pymongo.errors import (AutoReconnect,
                            ConnectionFailure,
                            ConfigurationError,
                            DuplicateKeyError,
                            InvalidOperation,
                            OperationFailure,
                            WTimeoutError)
from pymongo.read_preferences import ReadPreference
from pymongo.son_manipulator import SONManipulator
from test import (client_context,
                  client_knobs,
                  client_knobs_opts,
                  client_knobs_opts_ssl,
                  client_knobs_opts_ssl_cert_reqs_none,
                  client_knobs_opts_ssl_cert_reqs_none_ca_certs_none,
                  client_knobs_opts_ssl_cert_reqs_none_ca_certs_none_crlfile,
                  client_knobs_opts_ssl_cert_reqs_none_ca_certs_none
