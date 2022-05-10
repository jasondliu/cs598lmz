import socket
socket.if_indextoname(3)

import ctypes
from ctypes import wintypes

import sys

if sys.platform == 'win32':
    import win32file
    import win32event
    import pywintypes
    import winerror
    import winioctlcon
    import comtypes # for the GUID
    import comtypes.GUID
    from comtypes import GUID
    import comtypes.client
    import comtypes.server
    import comtypes.automation
    import comtypes.typeinfo
    import comtypes.gen
    import comtypes.IUnknown
    import comtypes.hresult
    import comtypes.COMError
    import comtypes.STA
    import comtypes.STAThread
    import comtypes.safearray
    import comtypes.POINTER
    import comtypes.BSTR
    import comtypes.automation
    import comtypes.shelllink
    import comtypes.persist
    import comtypes.persist.interfaces
    import comtypes.persist.interfaces.IPersistFile
    import comtypes.persist.interfaces.
