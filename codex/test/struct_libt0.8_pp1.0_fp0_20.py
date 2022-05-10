import _struct
import os
import re
import subprocess
import xml.etree.ElementTree
import uuid

_ifconfig_re = re.compile(r'^[\w]*? flags=\d+<((?:[A-Z]+[\d]*?,)*(?:[A-Z]+[\d]*?))> mtu (\d+)$')
