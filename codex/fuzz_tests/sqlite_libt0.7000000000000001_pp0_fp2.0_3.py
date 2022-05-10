import ctypes
import ctypes.util
import threading
import sqlite3
import traceback

# Importing maya.OpenMaya as OpenMaya
import maya.OpenMaya as OpenMaya
import maya.cmds as cmds
import maya.mel as mel

import pymel.core as pm
from pymel.core.system import Path

# Importing PyQt4 modules
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import uic

# Importing the Tactic module
from pyasm.common import Environment
from pyasm.biz import Project
from pyasm.search import Search
from pyasm.web import Table
from tactic_client_lib import TacticServerStub

# Importing the common files
from common import configuration
from common import constants

from file_reference_manager.common.file_reference_manager import FileReferenceManager
from file_reference_manager.common.shader_reference_manager import ShaderReferenceManager
from file_reference_manager.common.textures_reference_manager import TexturesReferenceManager
from file_reference_manager.common.cam_reference
