import types
types.ModuleType

import os
import sys
import unittest
import logging

from os.path import dirname, abspath

from pytest import raises

from testfixtures import LogCapture, ShouldRaise, compare

from pysimplesoap.client import SoapClient, SoapFault
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from pysimplesoap.simplexml import SimpleXMLElement

from . import server_base_address

# logging.basicConfig(level=logging.DEBUG)

# test server address
server_address = server_base_address + "/test_server"

# test client
client = SoapClient(
    location = server_address,
    action = server_address, # SOAPAction
    namespace = "http://example.com/sample.wsdl", 
    soap_ns='soap',
    ns = False)

# test dispatcher
