import signal
signal.signal(signal.SIGINT, signal_handler)

#wait for button click
flag = 1
while flag:
    val = GPIO.input(27)
    if val == 0:
        flag = 0

#quit from the program
GPIO.output(23, GPIO.LOW)
GPIO.cleanup()
