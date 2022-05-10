import signal
signal.signal(signal.SIGINT, signal_handler)

# Serial communication to arduino
def init_serial():
        try:
                ser = serial.Serial(
                        port='/dev/ttyACM0',
                        baudrate = 9600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1
                )
                return ser

        except:
                print "Error: could not connect to arduino"
                sys.exit()

# Send serial data to arduino
def serial_write(ser, data):
        ser.write(data)
        return

# Read serial data from arduino
def serial_read(ser):
        while True:
                if (ser.inWaiting() != 0):
                        data = ser.readline()
                        return data

# Read data from the serial port
def read_serial_data():
        data = serial_read(ser)
        split_data = data.split(',')
        new
