import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#Global variables
HasAccData = 0
HasGyrData = 0
HasMagData = 0

def main():

    # Define Variables
    global HasAccData
    global HasGyrData
    global HasMagData

    # Create sensor objects
    acc  = ADXL345()
    gyr  = ITG3200()
    mag  = HMC5883L()

    # Set sensitivity
    acc.setRange(ADXL345.RANGE_2G)
    gyr.setRange(ITG3200.RANGE_2000)
    mag.setRange(HMC5883L.RANGE_1_3GA)

    # Set data rate
    acc.setDataRate(ADXL345.DATARATE_100HZ)
    gyr.setDataRate(ITG3200.DATARATE_100HZ)
    mag.setDataRate(HMC5883L.DATARATE_75HZ)

   
