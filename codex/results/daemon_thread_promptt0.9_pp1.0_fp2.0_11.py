import threading
# Test threading daemon running
rd = threading.Thread(target=capture_and_display)
rd.setDaemon(True)  # Doesn't block the shell when running
rd.start()
ip = '127.0.0.1'
print ip
save_label = 0
# red_switch = 1

def on_press(key):
    global save_label
    try:
        print 'key file:', key.file, key.char
        # print 'key char:', key.char
        if key.char == ' ':
            print 'Got space!'
            # Save frame
            save_label ^= 1
            # print save_label
    except Exception, e:
        print e

with Listener(on_press=on_press) as listener:
    listener.join()
