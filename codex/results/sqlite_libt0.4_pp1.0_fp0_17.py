import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

class _GObject(ctypes.Structure):
    pass

class _GtkWidget(ctypes.Structure):
    pass

class _GtkWindow(ctypes.Structure):
    pass

class _GtkContainer(ctypes.Structure):
    pass

class _GtkBox(ctypes.Structure):
    pass

class _GtkButton(ctypes.Structure):
    pass

class _GtkLabel(ctypes.Structure):
    pass

class _GtkEntry(ctypes.Structure):
    pass

class _GtkTreeView(ctypes.Structure):
    pass

class _GtkListStore(ctypes.Structure):
    pass

class _GtkTreeViewColumn(ctypes.Structure):
    pass

class _GtkCellRendererText(ctypes.Structure):
    pass

class _GtkTreeSelection(ctypes.Structure):
    pass

class _GtkTreeIter(ctypes.Structure):
    pass

