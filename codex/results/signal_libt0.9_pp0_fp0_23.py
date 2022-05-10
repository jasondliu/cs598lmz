import signal
signal.signal(signal.SIGINT, signal_handler)

setup()

#LED OFF
GPIO.output(22,0)

print("Starting initialization...")

#Initialize empty matrix to store T/H sensor data
matrix = []

#Initialize empty matrix to store soil moisture data
soil_matrix = []

#Initialize empty matrix to store BME280 data
bme280 = []

#Initialize empty matrix to store GPS data
gps = []

#Read data every interval
interval = 15

#Total length of experiment (hours)
experiment_length = 3

#Set SEROUT pin high
GPIO.output(4,1)

print(time_to_end())

#This loop is the master loop that drives the whole experiment
while(time_to_end() > 0):

    #Collect data from T/H sensors
    data_humidity = []
    data_temperature = []
    for dhtpin in [2, 13]:
        dhtdev = adafruit_dht.DHT22(d
