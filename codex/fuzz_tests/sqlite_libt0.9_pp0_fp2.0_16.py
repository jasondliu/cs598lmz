import ctypes
import ctypes.util
import threading
import sqlite3

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Keywords'))

from strip_path_keyword import StripPathKeyword

APP_PATH = os.environ["PATH"]

FRAMEWORKS_PATH = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Frameworks')

for framework in os.listdir(FRAMEWORKS_PATH):
    if not os.path.isdir(os.path.join(FRAMEWORKS_PATH, framework)) or not framework.endswith('.framework'):
        continue
    if framework == 'libswiftAppKit.framework':
        continue

    sys.path.insert(0, os.path.join(FRAMEWORKS_PATH, framework, 'Resources'))

os.environ["PATH"] = APP_PATH

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '
