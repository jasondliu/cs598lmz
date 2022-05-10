import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#Gets the script directory
def getScriptDirectory():
    path = os.path.realpath(sys.argv[0]) # Get the file path
    path = os.path.split(path)[0] # Remove the file name
    return path

#Gets the time since epoch in microseconds
def getMicroTime():
    return int(round(time.time()*1000000))

#Prints a message to the console
def printToConsole(message, messageType = 'INFO'):
    print('[{0}][{1}] {2}'.format(getDate(), messageType, message))

#Prints a message to the console and saves it to a log file
def printToConsoleAndLog(message, messageType = 'INFO'):
    printToConsole(message, messageType)
    saveMessageToLog(message, messageType)

#Saves a message to the log file
def saveMessageToLog(message, messageType = 'INFO'
