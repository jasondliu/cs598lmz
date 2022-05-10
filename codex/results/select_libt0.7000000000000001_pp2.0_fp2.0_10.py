import select
from threading import Thread
from time import time, sleep
from typing import List, Tuple, Optional, Union, Dict
from urllib.parse import urlparse
from xml.etree.ElementTree import Element, ElementTree

from loguru import logger
from tornado.httpclient import AsyncHTTPClient, HTTPResponse

from . import exceptions
from .utils import (
    parse_options,
    parse_xml_body,
    dict_to_xml,
    get_ip_from_host,
    parse_headers,
    parse_http_protocol,
    parse_content_type,
    parse_xml_to_mapping,
)
from .utils import xpath_to_dict

__all__ = ("Response", "Request")

RESPONSE_OK = 200
RESPONSE_REDIRECT = 302

REQUEST_TIMEOUT = 30

METHODS = ("GET", "POST", "PUT", "DELETE")

HTTP_PROTOCOLS = ("HTTP/1.0", "HTTP/1.1", )


