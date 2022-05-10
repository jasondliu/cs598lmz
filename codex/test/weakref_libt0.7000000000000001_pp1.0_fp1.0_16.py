import weakref
import time
import os
import pickle
import numpy as np

from . import config, util, lldbutil, lldbcommands
from . import cmd as lldb_cmd, cmds as lldb_cmds

def get_lldb_version():
    v = util.exec_lldb_command('version').split('\n')[0].split()[-1]
    return [int(i) for i in v.split('.')]

def get_debugger_name():
    return "lldb"

def get_debugger_capabilities():
    """Return the debugger capabilities (the ones we use).
    
    This can vary from version to version, so we have to compute it on the fly.
    """
    caps = set()
    if get_lldb_version() >= [3, 8]:
        caps.add('python-prompt')
    return caps

