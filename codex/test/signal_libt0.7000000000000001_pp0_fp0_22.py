import signal
signal.signal(signal.SIGTERM, end_read)

def capture():
    global stop
    with open(home+"/data/rfid_log.txt", 'a+') as f:
        while not stop:
            if GPIO.input(GPIO_IRQ) == 0:
                response, cardType = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

                # If a card is found
