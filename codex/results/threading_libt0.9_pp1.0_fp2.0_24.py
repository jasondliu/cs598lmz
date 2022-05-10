import threading
threading.stack_size(17920)

def atan(x):
    """
    Arctangent function, returns angle in radians.
    x = tangent of angle
    """
    if x > 0:
        return math.atan(x)
    if x < 0:
        return math.atan(x)
    if x == 0:
        return 0

def gps_to_decimal(d, m, s):
    """
    Converts GPS coordenates (dd mm ss) to Decimal Degrees format (dd.dddddddd)
    d = degrees
    m = minutes
    s = seconds
    """
    return abs(d) + abs(m)/60+abs(s)/3600

def get_valid_coordinates(write_function, module_n, bus_rx, bus_current, bus_voltage):
    """
    Get the GPS coordinates from GPS module and send completed vectors to 'write_function'
    Returns None on failure, completed vector on success
    """
    # Global variables used
    global latitude, longitude
    global
