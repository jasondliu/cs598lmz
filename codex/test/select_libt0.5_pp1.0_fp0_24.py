import select
import socket
import sys
import time
import threading

# Попытка импорта модуля с возможностью работы с консолью
try:
    import msvcrt
except ImportError:
    msvcrt = None

# Попытка импорта модуля с возможностью работы с терминалом
try:
    import termios
except ImportError:
    termios = None


