import signal
signal.signal(signal.SIGINT, handler)

def get_time():
    return int(round(time.time()*1000))


def read_data():
    while True:
        data = ser.readline()
        try:
            if data[:2] == 'T,':
                return [float(x) for x in data[2:-1].split(',') if x != '']
        except Exception as e:
            print e

def read_data_str():
    return read_data().split(',')

def get_all_readings():
    data = read_data()
    readings = {'t_now' : get_time()}
    readings['x'] = data[0]
    readings['y'] = data[1]
    readings['z'] = data[2]
    readings['current'] = data[3]
    readings['open_angle'] = data[4]
    readings['closed_angle'] = data[5]
    readings['threshold_angle'] = data[6]
    readings['hall_position']
