import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
from ctypes.wintypes import *

OpenProcess = windll.kernel32.OpenProcess
GetCurrentProcess = windll.kernel32.GetCurrentProcess
WaitForSingleObject = windll.kernel32.WaitForSingleObject
K32EnumProcesses = windll.kernel32.K32EnumProcesses
K32EnumProcessModulesEx = windll.kernel32.K32EnumProcessModulesEx
K32GetModuleBaseName = windll.kernel32.K32GetModuleBaseNameA
K32GetModuleInformation = windll.kernel32.K32GetModuleInformation
K32GetModuleFileNameEx = windll.kernel32.K32GetModuleFileNameEx
K32TerminateProcess = windll.kernel32.TerminateProcess

SSLEEP = 2000

PROCESS_ALL_ACCESS = 0x1F0FFF
MEM_DECOMMIT = 0x4000
MEM_RELEASE = 0x8000
PAGE_READWRITE = 0x04
PAGE_EXECUTE_WRITECOPY = 0x80

