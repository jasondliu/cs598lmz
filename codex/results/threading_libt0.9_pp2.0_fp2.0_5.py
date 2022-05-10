import threading
threading.stack_size(67108864) # 64MB stack

SENSOR = 18
COUNT = 30

try:
    # read data using pin 18
    instance = MCP3008(channel=SENSOR)
    print 'Press Ctrl-C to quit...'
    while True:
        print(instance.value)
        time.sleep(1.0)

except KeyboardInterrupt:
    print "\nA keyboard interrupt has been noticed"

except:
    print "An error or exception has occurred!"

finally:
    GPIO.cleanup()
    print "\nAll GPIO pins have been cleaned up"
