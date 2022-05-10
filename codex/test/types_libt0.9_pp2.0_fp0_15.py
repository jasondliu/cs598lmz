import types
types.FunctionType = type

import pytest

from . import print_paths

def connect():
  host = 'a01'
  password = 'a01'
  db = 'e07'
  user = 'e07'
  port = 64528

  PROMPT = '-=[ mySQL ]=-'

  child = pexpect.spawn('ssh %s@%s -p %s' % (user, host, port), echo=False, timeout=15)
  i = child.expect([PROMPT, 'assword:', pexpect.TIMEOUT])
