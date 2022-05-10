import signal
signal.signal(signal.SIGINT, handler)

# Arduino serial port
sp = serial.Serial(port=sys.argv[1], baudrate=9600, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=0.5)

# Joystick
js = open(sys.argv[2], 'r')
max_axis = 32767
max_turn = 255

def forward(x):
    global sp
    global js
    global max_axis
    global max_turn

    speeds = [0, 0.90, 0.95, 0.98, 1.0]
    s = random.choice(speeds)
    x = int((x / 32767.0) * s * max_turn)
    sp.write(struct.pack('>B', 1)) # Manual mode
    sp.write(struct.pack('>B', 1))
    sp.write(struct.pack('>B', 1))
    sp.write(struct.pack('>B', -1 * x))

