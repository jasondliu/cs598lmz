import sys, threading
threading.Thread(target=lambda: sys.stdout.write('X' * 100000000)).start()

from hx711 import HX711
from scale import Scale
from sqlite3 import connect


# def cleanAndExit():
#     print "Cleaning..."
#     GPIO.cleanup()
#     print "Bye!"
#     sys.exit()

# Clean GPIO on exit
# atexit.register(cleanAndExit)

def getData_db(calibration_factor, weight_offset):
    try:
        scale = Scale(calibration_factor, weight_offset)
        print "Reading weight..."
        print scale.get_weight()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()

# main()
# while True:
#
#     if GPIO.event_detected(channel):
#          timestamp = datetime.datetime.now()
#          print('Button pressed at ' + str(timestamp))
#          getData_db(calibration_factor, weight_offset)

def getData_db_iter(calibration_factor,
