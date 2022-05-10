import ctypes
import ctypes.util
import threading
import sqlite3
import traceback
import sys
import os
import platform

# Modules included in this file:
# Currently defines Resource, ResourceNode, and ResourceSet
################################################################################

################################################################################
# Classes:
################################################################################
class ResourceNode(object):
    def __init__(self):
        self.res_set = ResourceSet()
        self.associations = []
        self.name = ""
        self.file = None
        self.fileBuffer = None
        self.id = 0
        self.category = ""

    # associate a resource with this node
    def associate(self, res):
        self.res_set.add(res)

    def unassociate(self, res):
        if res in self.res_set:
            self.res_set.remove(res)

    # return all associated resources
    def getResSet(self):
        return self.res_set

class Resource(object):
    resource_id_lock = threading.Lock()
    active_res_lock = threading.Lock()
