import _struct

# Create a streamer
streamer = Streamer(bucket_name=BUCKET_NAME,
                    bucket_key=BUCKET_KEY,
                    access_key=ACCESS_KEY)

while True:
    T = _struct.unpack("d",ser.read(8))[0]
    H = _struct.unpack("d",ser.read(8))[0]
    P = _struct.unpack("d",ser.read(8))[0]
    print([T,H,P])
    streamer.log("Temperature", T)
    streamer.log("Humidity", H)
    streamer.log("Pressure", P)
    time.sleep(1)
