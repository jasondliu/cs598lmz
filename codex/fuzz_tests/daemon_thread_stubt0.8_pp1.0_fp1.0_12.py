import sys, threading

def run():
    if debug: print "Run"
    try:
        ws = websocket.create_connection(getConfig('webSocketUrl'))
        ws.send(json.dumps({'topic':'login', 'token':getConfig('webSocketToken')}))
        while True:
            message = ws.recv()
            if message:
                obj = json.loads(message)
                if debug: print obj
                handleWebsocketMessage(obj)
            else:
                break
    except Exception as e:
        print e
        ws.close()

def handleWebsocketMessage(obj):
    if obj['topic'] == 'player':
        if obj['id'] == getConfig('id'):
            playerEvent(obj['event']);

def playerEvent(event):
    if event == 'play': play()
    elif event == 'pause': pause()
    elif event == 'toggle': toggle()
    elif event == 'restart': restart()
    elif event == 'stop': stop()
    elif event == 'volup': volup
