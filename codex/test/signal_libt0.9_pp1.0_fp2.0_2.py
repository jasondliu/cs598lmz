import signal
signal.signal(signal.SIGINT, handler)

def main(args):
    global continue_reading
    prev_datapoints = [None, None]
    # 200 samples per second
    hz = 200
    sample_time = 1/200
    w = fftfreq(hz, sample_time)
    i = 0
    txt_file = open(args.filename, 'w')
    txt_file.write('time' + ',' + 'data' + '\n')
    num_seconds = args.num_seconds
    start_time = time.time()
    # Initialise the device
    rdr = RFID(device='tty:AMA0:pn532', antenna=2)
    user_input = ''
