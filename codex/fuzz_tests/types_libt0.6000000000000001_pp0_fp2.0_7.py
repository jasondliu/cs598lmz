import types
types.FunctionType = types.BuiltinFunctionType

import os
import sys
import json
import subprocess
import inspect
import traceback
import threading

import sublime
import sublime_plugin

try:
    from GitGutter.git_gutter_handler import GitGutterHandler
    GITGUTTER_PRESENT = True
except ImportError:
    GITGUTTER_PRESENT = False

# debug
DEBUG = False

# settings
SETTINGS_FILE = "SublimeGHCi.sublime-settings"

# ghci
GHCI_CMD = "ghci"

# ghci commands
GHCI_CMD_LOAD = ":load"
GHCI_CMD_RELOAD = ":reload"
GHCI_CMD_TYPE = ":type"
GHCI_CMD_KIND = ":kind"
GHCI_CMD_INFO = ":info"
GHCI_CMD_BROWSE = ":browse"
GHCI_CMD_SET = ":set"
GHC
