import signal
signal.signal(signal.SIGINT, signal_handler)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

while True:

    # Scan for cards
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print("Card detected")

    # Get the UID of the card
    (status, uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))

        # This is the default key for authentication
        key = [0xFF, 0xFF, 0xFF
