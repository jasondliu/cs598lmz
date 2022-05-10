import gc, weakref

from WMCore.Services.WMStats.WMStatsReader import WMStatsReader
from WMCore.Services.PhEDEx.PhEDEx import PhEDEx
from WMCore.Services.DBS.DBSErrors import DBSReaderError
from WMCore.WMException import WMException

def getWMStatsReader(couchURL, reqdbURL, config):
    """
    Get WMStatsReader from WMStatsReader module
    """
    wmstatsReader = WMStatsReader(couchURL, reqdbURL, config)
    return wmstatsReader

def getWMBSHelper(dbi, group="Analysis",
                  couchURL='https://cmsweb.cern.ch/couchdb', couchapp="WMStats"):
    """
    Get WMBS Helper from WMBSHelper module
    """
    wmbsHelper = WMBSHelper(dbi, couchURL, couchapp, group)
    return wmbsHelper

def getWMSpecFromWMStats(reqmgrdbURL, requestName):
    """
    Get WMSpec from WMStats
    """
    spec
