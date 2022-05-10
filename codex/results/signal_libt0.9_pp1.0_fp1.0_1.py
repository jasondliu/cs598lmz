import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # allow CTRL+C interrupt

while True:
    os.system('clear') # clear terminal screen
    inputs = uart.read(1)
    if inputs:
        inputs = binascii.hexlify(inputs)
        inputs = str(inputs, "UTF-8")
        print(inputs)

uart.close()
