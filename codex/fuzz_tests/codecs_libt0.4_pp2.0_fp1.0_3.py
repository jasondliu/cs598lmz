import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import sys
import os
import re
import json
import time
import datetime
import traceback
import logging
import logging.config

import requests
from pyquery import PyQuery as pq

from libs.utils import get_html_by_requests as get_html
from libs.utils import get_html_by_selenium as get_html_selenium
from libs.utils import get_html_by_requests_proxy as get_html_proxy
from libs.utils import get_html_by_selenium_proxy as get_html_selenium_proxy
from libs.utils import get_html_by_selenium_phantomjs_proxy as get_html_selenium_phantomjs_proxy
from libs.utils import get_html_by_selenium_phantomjs as get_html_selenium_phantomjs
from libs.utils import get_html_by_selenium_phantomjs_with_js as get_html_
