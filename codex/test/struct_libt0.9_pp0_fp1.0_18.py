import _struct
import struct
import platform
import time
import ctypes


class CTCIthread(threading.Thread):
    def __init__(self, gpas, stop_event):
        super(CTCIthread, self).__init__()
        self.stop_event = stop_event
        # self.gpas = gpas

    def run(self):
        vci_device_type = 4  # USBCAN2
        vci_device_ind = 0
        can_port = 1
        start_channel = 0
        filter = 0
        baud = 0
        self.g_bOpen = 0

        # CAN diag: Filter
        # CAN_INIT_TYPE_EX = 3
        CAN_INIT_TYPE_EX = 4
        self.g_bOpen = VCI_OpenDevice(
            vci_device_type, vci_device_ind, 0)
        if self.g_bOpen == 1:
            log.debug('Open SUCCESS!\n')
            config = VCI_INIT_CONFIG()
