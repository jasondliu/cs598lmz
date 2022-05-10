import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

import os
import sys
import socket
import sys
import win32api
import win32service
import win32serviceutil
import win32event
import servicemanager
import win32pipe

class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "DJANGO"
    _svc_display_name_ = "Django Web Application Server"
    _svc_description_ = "Django application server"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EV
