import signal
signal.signal(signal.SIGINT, signal_handler)

#Create objects for each of the devices.
#QT_ATM_4850_1 = ATM4850(1)
#QT_ATM_4850_2 = ATM4850(2)
#QT_ATM_4850_3 = ATM4850(3)
QT_ATM_4850_4 = ATM4850(4)

#QT_ATM_4850_1.set_current(.1)
#QT_ATM_4850_2.set_current(.1)
#QT_ATM_4850_3.set_current(.1)
QT_ATM_4850_4.set_current(.1)

#QT_ATM_4850_1.get_current()
#QT_ATM_4850_2.get_current()
#QT_ATM_4850_3.get_current()
QT_ATM_4850_4.get_current()

try:
	
