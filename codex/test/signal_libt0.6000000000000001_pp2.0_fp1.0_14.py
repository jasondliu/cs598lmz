import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# init global variables
def initGlobalVars():
    global g_serial_port
    global g_serial_baud
    global g_serial_timeout
    global g_serial_bytesize
    global g_serial_parity
    global g_serial_stopbits
    global g_serial_xonxoff
    global g_serial_rtscts
    global g_serial_dsrdtr
    global g_serial_write_timeout
    global g_serial_inter_byte_timeout
    global g_serial_port_name
    global g_serial_port_handle
    global g_serial_connected
    global g_serial_status_error
    global g_serial_status_error_msg
    global g_serial_status_line_endings
    global g_serial_status_line_endings_msg
    global g_serial_status_baud_rate
    global g_serial_status_parity
    global g_serial_status_stopbits
    global g_
