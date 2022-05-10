import select
import struct
import socket

MODEMDEVICE = '/dev/ttyACM0'
BAUDRATE = 19200

def open_modem( modem_device = MODEMDEVICE, baudrate = BAUDRATE):
    modem = serial.Serial()
    modem.port = modem_device
    modem.baudrate = baudrate
    modem.bytesize = serial.EIGHTBITS
    modem.parity = serial.PARITY_NONE
    modem.stopbits = serial.STOPBITS_ONE
    modem.xonxoff = 0
    modem.rtscts = 0
    modem.timeout = 20
    modem.writeTimeout = 20
    modem.open()
    return modem

def send_at_command( modem, at_command ):
    """Send an AT command to the modem (assumed to be open) and wait for an
    output response.  The 'wait' is a bit of a lie, because the modem may
    or may not respond to the AT command, and there may or may not be
    characters waiting in the serial buffer.

   
