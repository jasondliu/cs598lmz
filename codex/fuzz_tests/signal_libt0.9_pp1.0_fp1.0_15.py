import signal
signal.signal(signal.SIGINT, signal_handler)

# Initiate I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize camera
camera = init_camera()

# Read in config file
conf = read_config(CONFIG_LOC)

# Initialize temperature sensor
temp_sensor = init_temp_sensor(i2c, conf)

# Initialize water sensor
water_sensor = init_water_sensor(i2c, conf)

# Initialize light sensor
light_sensor = init_light_sensor(i2c, conf)

# Initialize buzzer
buzzer = init_buzzer(i2c, conf)

# Start a server
app = Flask(__name__)

# We want to turn off the auto reloading because we are running a
# continuous while loop that runs the raspberry pi camera.
app.config['DEBUG'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = False


@app.
