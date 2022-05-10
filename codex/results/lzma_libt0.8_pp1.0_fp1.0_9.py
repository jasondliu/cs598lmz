import lzma
lzma.open

# extract_artifact.py
import subprocess
subprocess.Popen().communicate

# i18n.py
import gettext
gettext.translation('messages', 'locale').gettext

# ipc_without_perms.py
import gconf
gconf.client_get_default

# popen_with_overflow.py
import subprocess
subprocess.Popen().communicate

# popen_with_overflow2.py
import subprocess
subprocess.Popen().communicate

# socket.py
import socket
socket.socket().connect_ex

# socket_with_port.py
import socket
socket.socket().connect_ex

# sqlite3_shell.py
import sqlite3
sqlite3.connect

# subprocess_with_overflow.py
import subprocess
subprocess.Popen().communicate

# untrusted_pickle.py
import pickle
pickle.load

# untrusted_yaml.py
import yaml
yaml.load
