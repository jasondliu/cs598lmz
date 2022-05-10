import threading
# Test threading daemon

def func(a,b):
    print (a+b)
    time.sleep(1)
    print ("Done")

# Create thread
t1 = threading.Thread(target=func, args=(1,2))

# Set daemon
t1.setDaemon(True)

# Start thread
t1.start()

print ("End")

# If you comment out the above line "t1.setDaemon(True)"
# then the output would be
# End
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done
# 3
# Done

