import select
import fcntl
import sys
import os

from vyos.config import Config
from vyos.util import call
from vyos import ConfigError


def get_config():
    c = Config()
    base = ['interfaces', 'bridge']
    if not c.exists(base):
        return None

    # read all bridge interfaces currently configured
    bridge_if = c.return_values(base)
    conf = {'name': [], 'member': [], 'type': '', 'base': base}
    for ifname in bridge_if:
        c.set_level(base + [ifname])
        conf['name'].append(ifname)
        conf['member'].append(c.return_values('member'))
        conf['type'] = c.return_value('type')
        conf['stp'] = c.return_value('stp')

    return conf

def verify(conf):
    if not conf:
        return None

    # ensure type is set
