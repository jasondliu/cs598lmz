import signal
signal.signal(signal.SIGINT, handler)
# import time
# from luma.core.serial import spi, noop
# from luma.core.render import canvas
# from luma.led_matrix.device import max7219

# def x(value):
#     device = max7219(spi(port=0, device=0, gpio=noop()), cascaded=1)
#     while True:
#         with canvas(device) as draw:
#             draw.point((value,0), fill="white")
#             time.sleep(0.04)


# x(10.0)

#------------------------------------------------------------------------------------------
# import time
# from bluetooth import *

# print "performing inquiry..."

# nearby_devices = discover_devices(lookup_names = True)


# # print "found %d devices" % len(nearby_devices)

# for addr, name in nearby_devices:
#     print " %s - %s" % (addr, name)
    # serv = find_service(name = "set
