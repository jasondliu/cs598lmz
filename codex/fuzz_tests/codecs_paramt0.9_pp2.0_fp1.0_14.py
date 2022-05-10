import codecs
codecs.register_error("skip",lambda e:("",e.end))

myLogFile = "[ ]"

gyro_data = []
mag_data = []
acc_data = []
pres_data = []
temp_data = []
gyr_avg = [0,0,0]
mag_avg = [0,0,0]
acc_avg = [0,0,0]
pres_avg = 0.0
temp_avg = 0.0

def processFile(name):
    print "Processing file ", name, "..."
    global gyro_data
    global mag_data
    global acc_data
    global pres_data
    global temp_data
    global gyr_avg
    global mag_avg
    global acc_avg
    global pres_avg
    global temp_avg
    for i in range(0,len(gyro_data)):
        for j in range(0,3):
            if abs(gyro_data[i][j]) > 0.05:
                gyr_avg[j] +=
