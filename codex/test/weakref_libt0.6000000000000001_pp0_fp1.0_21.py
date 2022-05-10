import weakref
import traceback
import os
import sys
import threading
import time
import collections
import copy
import logging
import socket
import re
import json

import six

import pytest

import pykka
import pykka.actor
import pykka.exceptions
import pykka.future
import pykka.registry
import pykka.threading
import pykka.util

if sys.version_info[0] < 3:
    from mock import patch, Mock, MagicMock
    from StringIO import StringIO
else:
    from unittest.mock import patch, Mock, MagicMock
    from io import StringIO


def test_actor_has_empty_references_after_init():
    actor_ref = ActorRefMock()
    actor = pykka.actor.Actor(actor_ref)
