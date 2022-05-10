import select
# Test select.select()

readQueue,writeQueue=[],[]
running=True

while running:
    readable,writeable,exceptions=select.select(readQueue,writeQueue,[])
    for sockObj in readable:
        data=sockObj.recv(1024)
        if not data:
            sockObj.close()
            readQueue.remove(sockObj)
        else:
            print("Recived ",data) # Show data recived.
    for sockObj in writeable:
        try:
            nextSend=nextSay[sockObj]
        except KeyError:
            pass
        else:
            nextSay[sockObj]=nextSend[len(sockObj.send(nextSend)):] # Send as much as possibl.
        if not nextSay:
            writeQueue.remove(sockObj)
