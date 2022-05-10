import sys, threading

def run():
    e32.ao_sleep(0.2)
    print "Running"
    appuifw.note(u"Sleeping for 10 seconds...", "info")
    e32.ao_sleep(10)
    print "Woke up"
    appuifw.note(u"Woke up", "info")

def exit_key_handler():
    app_lock.signal()

app_lock = e32.Ao_lock()
thread = threading.Thread(target=run)
thread.start()

print "This is the main program thread"
print "Press Options to exit"
appuifw.app.exit_key_h
