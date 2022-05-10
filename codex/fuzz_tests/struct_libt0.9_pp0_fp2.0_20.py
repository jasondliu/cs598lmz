import _struct


class py_hci(object):
    def __init__(self):
        self.hci_socket = -1
        self.hci_iface = -1
        self.hci_dev = -1
        self.hci_diag = -1
        self.status_codes = {
        0x00:'Success',
        0x01:'Unknown HCI Command',
        0x02:'Unknown Connection Identifier',
        0x03:'Hardware Failure',
        0x04:'Page Timeout',
        0x05:'Authentication Failure',
        0x06:'PIN/Key Missing',
        0x07:'Memory Capacity Exceeded',
        0x08:'Connection Timeout',
        0x09:'Connection Limit Exceeded',
        0x0A:'Synchronous Connection Limit To A Device Exceeded',
        0x0B:'ACL Connection Already Exists',
        0x0C:'Command Disallowed',
        0x0D:'Connection Rejected due to Limited Resources',
        0x0E:'Connection Rejected Due To Security Reasons',
        0x
