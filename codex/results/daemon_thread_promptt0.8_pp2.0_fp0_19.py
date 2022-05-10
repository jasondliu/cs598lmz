import threading
# Test threading daemon
def deamon():
    print('start deamon')
    time.sleep(2)
    print('end deamon')

def nonDeamon():
    print('start nonDeamon')
    print('end nonDeamon')

#d = threading.Thread(name = 'deamon',target = deamon)
d = threading.Thread(name = 'deamon',target = deamon,daemon=True)
t = threading.Thread(name = 'nonDeamon',target = nonDeamon)

d.start()
t.start()
