import signal
signal.signal(signal.SIGTERM, end_read)

def capture():
    global stop
    with open(home+"/data/rfid_log.txt", 'a+') as f:
        while not stop:
            if GPIO.input(GPIO_IRQ) == 0:
                response, cardType = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

                # If a card is found
                if response == MIFAREReader.MI_OK:
                    print "Card detected"
                    f.write("Card detected\n")

                # Get the UID of the card
                (status,uid) = MIFAREReader.MFRC522_Anticoll()

                # If we have the UID, continue
                if status == MIFAREReader.MI_OK:

                    # Print UID
                    print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
