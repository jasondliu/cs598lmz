import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def import_modules():
    import sys, os, imp
    from os.path import join, isdir
    from os import listdir
    from os import walk
    from os import path
    from os.path import dirname, abspath
    from os.path import basename
    from os.path import splitext
    from os.path import expanduser
    from os.path import isfile
    from os import getcwd
    from os import chdir
    from os import makedirs
    from os import remove
    from os import environ
    from os import system
    from os import linesep
    from os import name
    from os import devnull
    from os import fdopen
    from os import open
    from os import close
    from os import mkdir
    from os import rmdir
    from os import walk
    from os import getenv
    from os.path import exists
    from os.path import isdir
    from os.path import isfile
