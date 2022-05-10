import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import os.path
import argparse
import subprocess
import re

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs, flush=True)

def run(cmdbuild, cwd=None):
    if cwd is None:
        cwd = os.getcwd()
    exe = cmdbuild[0]
    pro = popen_stdout(cmdbuild, cwd=cwd)
    if pro.returncode != 0:
        raise RuntimeError('FAIL: %s in %s' % (exe, cwd))

def run_output(cmdbuild, cwd=None):
    if cwd is None:
        cwd = os.getcwd()
    exe = cmdbuild[0]
    pro = popen
