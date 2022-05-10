import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(process_id)

import sys
#sys.stdout = open(os.path.join(os.path.dirname(__file__), r'C:\Logs\PSSMasterService.txt'), 'w')


class Service(win32serviceutil.ServiceFramework):
    """
    Service class for the Windows PSSMaster Service
    """
    _svc_name_ = "PSSMasterService"
    _svc_display_name_ = "PSS Header Service"
    _svc_description_ = "Service to run PSS Header"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop
