import threading
# Test threading daemon mode using the sleep function
sthd = threading.Thread(target = sleep_thread, args = ("Sleep Thread", 2))
sthd.setDaemon(True)
sthd.start()

st = time.time()
time.sleep(1)
et = time.time()
print("Main thread sleep time:%s" % (et - st))

print("Main thread ended")


# Test threading daemon mode using busy loop
sthd = threading.Thread(target = busy_loop, args = ("Busy Loop", 2))
sthd.setDaemon(True)
sthd.start()
 
st = time.time()
time.sleep(1)
et = time.time()
print("Main thread sleep time:%s" % (et - st))

print("Main thread ended")
 
 
# Test threading daemon mode using waiting thread event to shutdown itself
stop_event = threading.Event()
sthd = threading.Thread(target = wait_event, args = ("Event Wait Loop", 2, stop_event))
sthd.setDaemon(True)
