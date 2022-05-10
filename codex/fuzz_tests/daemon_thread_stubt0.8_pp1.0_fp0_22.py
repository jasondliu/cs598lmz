import sys, threading

def run():
    pykd.dbgCommand("bp ntdll!DbgUiRemoteBreakin ")
    pykd.go()
    global thread_id
    thread_id = pykd.getThreadId()
    print "Thread ID  " + str(thread_id)

def breakpoint_handler(bp):
    pykd.dbgCommand("bl")
    pykd.dbgCommand("bp ntdll!DbgUiRemoteBreakin ")
    attach_to_process(pykd.getCurrentProcessId())
    pykd.go()
    pykd.dbgCommand("~2 s")
    print "Thread ID  " + str(thread_id)
    pykd.dbgCommand("~2 g")
    pykd.bpHandlerDone()

def attach_to_process(pid):
    command = "~" + str(thread_id) + "s"
    pykd.dbgCommand("~" + str(thread_id) + "s")
    pykd.dbgCommand("!load unh
