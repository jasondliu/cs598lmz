import gc, weakref
import os, sys, stat, os.path, glob
import time
import struct
import traceback
import imp, pickle
import textwrap

import gtk, gobject
import pango

from . import common, config, prefs, dialogs, thumbnails, pixbufs, \
     fileops, fileicons, fileinfo, fileview, history, \
     bookmark, catalog, catalogs, filemanager, undo, undo_manager
from . import i18n
_ = i18n.language.gettext

def _get_file_list_selection(listview):
    return [item.data.path
            for item in listview.get_selected_items()
            if isinstance(item.data, filelist.FileListItem)]

def _set_file_list_selection(listview, paths):
    listview.select_all()
    listview.unselect_all()
    for item in listview.get_items():
        if isinstance(item.data, filelist.FileListItem) and item.data.path in paths:
            item.set
