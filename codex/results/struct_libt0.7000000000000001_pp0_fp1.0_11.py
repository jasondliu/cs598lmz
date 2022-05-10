import _struct
from _struct import unpack
from _struct import calcsize
from _struct import pack
from _array import array

from sys import getsizeof
import sys
from sys import argv
from sys import exit
from sys import stdin
from sys import stdout
from sys import stderr
from sys import maxunicode
from sys import platform as sys_platform
from sys import version_info as sys_version_info

from os import environ
from os import getenv
from os import makedirs
from os import remove
from os import remove as delete
from os import rmdir
from os import rename
from os import stat
from os import system
from os import uname
from os import getcwd
from os import chdir
from os import getpid
from os import getppid
from os import waitpid
from os import linesep as os_linesep
from os import path as os_path
from os import listdir
from os import fdopen
from os import utime
from os import kill
from os import pipe
from os import dup2
from os import spawnv
from os import exec
