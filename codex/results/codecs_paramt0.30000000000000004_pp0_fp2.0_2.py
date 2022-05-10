import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

import os
import sys
import logging

from optparse import OptionParser

from traits.api import HasPrivateTraits, Str, Bool, List, Instance, \
                                 Property, cached_property, on_trait_change

from apptools.preferences.api import Preferences

from .api import File, Directory
from .file_info import FileInfo
from .file_system_path import FileSystemPath
from .file_system_name import FileSystemName
from .file_system_content import FileSystemContent
from .file_system_metadata import FileSystemMetadata
from .file_system_preferences import FileSystemPreferences
from .file_system_cache import FileSystemCache
from .file_system_actions import FileSystemActions
from .file_system_node import FileSystemNode

from .file_system_content_viewer import FileSystemContentViewer
from .file_system_content_editor import FileSystemContentEditor
from .file_system_metadata_
