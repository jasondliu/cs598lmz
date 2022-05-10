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
  if i == 1:
    child.sendline(password)
    j = child.expect([PROMPT, pexpect.TIMEOUT])
    if j == 1:
      raise ValueError('Host could not validate password')

  child.sendline('mysql -u %s -p' % user)
  i = child.expect(['assword:', pexpect.TIMEOUT])
  if i == 0:
    child.sendline(password)
    j = child.
