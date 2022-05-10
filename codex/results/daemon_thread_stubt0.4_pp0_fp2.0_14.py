import sys, threading

def run():
    global g_RscRC
    global g_RscObj
    global g_RscClient
    global g_RscServer
    global g_RscMsg
    global g_RscMsgMgr
    global g_RscMsgMgrClient
    global g_RscMsgMgrServer

    g_RscRC = RscRC()
    g_RscObj = RscObj()
    g_RscClient = RscClient()
    g_RscServer = RscServer()
    g_RscMsg = RscMsg()
    g_RscMsgMgr = RscMsgMgr()
    g_RscMsgMgrClient = RscMsgMgrClient()
    g_RscMsgMgrServer = RscMsgMgrServer()

def init():
    global g_RscRC
    global g_RscObj
    global g_RscClient
    global g_RscServer
    global g_RscMsg
    global g_RscMsgMgr
    global g_RscMsgMgrClient
    global g_R
