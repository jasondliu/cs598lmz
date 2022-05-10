import select
# Test select.select(), with and without signal handling

import os, select, signal, sys, time

signal.signal(signal.SIGINT, signal.SIG_IGN)

