import select
# Test select.select()
print(select.select([], [], []))

import re
# Test re.compile()
print(re.compile("foo"))

import sys
# Test sys.stdout
print(sys.stdout)

import time
# Test time.sleep()
time.sleep(1)

import urllib.request
# Test urllib.urlopen()
print(urllib.request.urlopen("http://example.com/"))

import zlib
# Test zlib.compress()
print(zlib.compress("foo"))

# Test ast.literal_eval()
import ast
print(ast.literal_eval("1 + 2"))

# Test argparse.ArgumentParser()
import argparse
print(argparse.ArgumentParser())

# Test base64.b64decode()
import base64
print(base64.b64decode(""))

# Test bisect.bisect_left()
import bisect
print(bisect.bisect_left([], 1))

# Test calendar.monthrange()

