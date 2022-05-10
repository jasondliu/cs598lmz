import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def Scan():
    scanner_list = scan("/dev/ttyUSB*", 57600)
    return scanner_list

def Scan_Time(Time):
    scanner_list = scan("/dev/ttyUSB*", 57600, Time)
    return scanner_list

def Open(name):
    scanner = Serial(name, 57600)
    return scanner

def Send(scanner, cmd):
    scanner.write(cmd+'\n')
    data = scanner.readline()
    return data

def Close(scanner):
    scanner.close()
    return

def Scan_Close(scanner_list):
    for s in scanner_list:
        s.close()
    return
