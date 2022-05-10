import threading
# Test threading daemon

#def printit():
#    threading.Timer(5.0,printit).start()
#    print("Hello, World!")
#
#printit()

# Test promise and following loop
#def printit():
#    threading.Timer(1.0,printit).start()
#    print("Hello, World!")
#
#printit()
#
#while True:
#    print(1)

# Test threading non-daemon
#def fun_timer():
#    print 'Hello Timer!'
#
#timer = threading.Timer(3, fun_timer)
#timer.start()

# Test threading daemon
def printit():
    threading.Timer(5.0,printit).start()
    print("Hello, World!")

threading.Thread(target=printit).start()
print("I'm still working")
