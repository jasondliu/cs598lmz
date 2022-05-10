import signal
signal.signal(signal.SIGINT, signal_handler)
#%%
# Create serial I/O object
try:
    sio = serial.Serial('/dev/tty.usbserial-DN0092RW',19200,timeout=10)
except:
    sio = serial.Serial('/dev/tty.usbmodemfd121',19200,timeout=10)
if not sio.isOpen():
    sio.open()

#%% Read RVC data and send as ROS messages

topic_name = "/us"
pub = rospy.Publisher(topic_name,Utm)
rospy.init_node('rvc_tracker',anonymous=True)
rate = rospy.Rate(4.9)

while not rospy.is_shutdown():
    # Read from serial port
    try:
        # Read from serial port
        sio_data = sio.readline()
        # Parse string into list
        sio_data = sio_data.split(',')
    except:
        print 'Unable to
