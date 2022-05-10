import _struct
import time
import test_config

def main():
    #connect to aion
    bus = _c.Bus();
    aion = _c.Aion(bus);
    if not aion.open():
        print "unable to open"
        return 1

    #open DIO1
    dio = aion.dio(1)
    if not dio.open():
        print "unable to open DIO1"
        return 1
    
    #read the initial state
    s = dio.getState()
    print "initial state: %s" % s

    #configure a pin to be an output
    if not dio.setMode(1, _c.DIO_OUTPUT):
        print "unable to set pin 1 to output"
        return 1

    #change the state of the pin
    if not dio.setState(1, 1):
        print "unable to set pin 1 to 1"
        return 1

    #toggle
    if not dio.toggle(1):
        print "unable to toggle pin 1
