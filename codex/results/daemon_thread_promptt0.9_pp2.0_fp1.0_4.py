import threading
# Test threading daemon
import re
import subprocess
import os
# Migrate to this at some point?
#

class dnsLookup(object):
  def __init__(self, hostname):
    if not hostname:
      raise Exception("No hostname")
    if re.match('^[-\.a-z0-9]+$', hostname):
      self.hostname = hostname
    else:
      raise Exception("Invalid hostname")

  def whoisHostname(self, hostname):
    cmdline = ["whois", "-H", hostname]
    p = subprocess.Popen(cmdline, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    if p.returncode != 0:
      raise Exception("Whois failed for %s" % hostname)
    return output

  def lookupName(self, name):

    print("%s %s" % (threading.currentThread().getName(), name))
    try:
      data = self.whoisHostname(name)
      if data:
        print("
