import threading
# Test threading daemon
# Use this to test with multiple clients
import time
from SyslogProcessing import SyslogProcessing
from DeviceConfigurationProcessing import DeviceConfigurationProcessing
from DeviceChangeRuleProcessing import DeviceChangeRuleProcessing
from ReadMEFData import ReadMEFData
from MEFTableProcessing import MEFTableProcessing
import pandas as pd

#Client Number Global
clientCount = 0;
clientCountGlock = threading.Lock();
"""
Function to process the data sent by the client and send response back
"""
def processClientData(data, connection):
    try:
        print " In processClientData Function "
       
        results = {};    # Stores the results of the Client Request
        global clientCount
        global clientCountGlock
        resultsJson = {};     # Results variable converted to Json
        wait = 0;
        clientCountGlock.acquire();
        if(clientCount >= 6):
            wait = 1;
            print "Number of clients more than 4 : "+str(clientCount);
        if(wait == 0):
            clientCount += 1;
            print
