import _struct
import traceback
import uuid

# Data Structures
class SLAData():
    RequestID = ""
    RequestName = ""
    RequestUpdateDate = []
    RequestStatus = ""
    RequestLastModifiedDate = -1.0
    def __init__(self):
        self.RequestID = ""
        self.RequestName = ""
        self.RequestUpdateDate = []
        self.RequestStatus = ""
        self.RequestLastModifiedDate = -1.0
    def __str__(self):
        _s = """
        RequestID                   : {0}
        RequestName                 : {1}
        RequestUpdateDate           : {2}
        RequestStatus               : {3}
        RequestLastModifiedDate     : {4}
        """.format(self.RequestID, 
                   self.RequestName, \
                   self.RequestUpdateDate, \
                   self.RequestStatus, \
                   self.RequestLastModifiedDate)
        return _s
    def __dict__(self):
        _d = {}
