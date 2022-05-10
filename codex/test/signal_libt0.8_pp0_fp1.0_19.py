import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # Ctrl + C Exits the program

# Find CaloCalibration CSC
CalibCSC=False
for strip in stripList:
  if strip.det=="ECAL":
    CalibCSC=True
    break

# Process the event
while True:
  event = eventIterator.next()
  if event is None:
    break # end of file
