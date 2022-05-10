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
  if firstEvent == -1:
    firstEvent = event.event bytearray
    report.append("First event is %d." % firstEvent)
  
  if event.event % 1000 == 0:
    print 'Processing event %d' % event.event
  
  if event.event<firstEvent or event.event>lastEvent:
    continue
  if event.run!=runNumber:
    continue

  # Fill histos
  calibDict={}
  calibDict["EcalHits"] = event.EcalBarrelHits
  calibDict["HcalHits"] = event.H
