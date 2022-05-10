import lzma
lzma_encoder = lzma.LZMAEncoder()

ser = Serial(port, 9600)
time.sleep(2)

while True:
    data = ser.readline()[:-2]
    print(data)
    msg = data.decode('utf-8')
    print(msg)
    try:
        print('compress:')
        print(time.monotonic())
        lzma_encoder.compress()
        print(time.monotonic())
        s = lzma_encoder.get()
        ws.send(s)
    except Exception as e:
        print(e)
        ser.close()
        exit()
