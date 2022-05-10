import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect from a thread
# The thread must create and manage a custom sqlite3.Connection object.
#    conn = sqlite3.connect(':memory:', check_same_thread=False)
# The thread must call conn.close() explicitly.
#    conn.close()

##############################################################################
# TEST GLOBALS
##############################################################################
bTEST_LOG = False
g_test_names = []
g_test_results = []

# The test should always run in the current work directory,
# and that directory should always be the one that python was
# called from on the command line.
START_DIR = os.getcwd()

##############################################################################
# TEST FUNCTIONS
##############################################################################
def ResetResults():
    global g_test_names
    global g_test_results
    g_test_names = []
    g_test_results = []

def Test(test_name, result):
    global g_test_names
    global g_test_results
    g_test_names.append(test_name)
    g
