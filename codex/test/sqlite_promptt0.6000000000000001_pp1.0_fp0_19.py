import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:', check_same_thread=False)
import time

import  wx
import  wx.lib.buttons  as  buttons
import  wx.lib.mixins.listctrl  as  listmix

import  images
import  CNavigationBar
import  CTextCtrlAutoComplete

import  CBaseMangaReaderFrame
import  CBaseMangaReaderFrameAddMangaDialog
import  CBaseMangaReaderFrameAddMangaDialogAddMangaPanel
import  CBaseMangaReaderFrameAddMangaDialogAddMangaPanelGenresPanel

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class CMangaReaderFrame(CBaseMangaReaderFrame.CBaseMangaReaderFrame):
    def __init__(self, parent):
        CBaseMangaReaderFrame.CBaseMangaReaderFrame.__init__(self, parent)

        self.m_navigationBar.SetSelection(1)
        self.m_navigationBar.Refresh()

