import signal
signal.signal(signal.SIGINT, signal_handler)

while True:
    _ = input("Press Enter to update...")
    try:
        ap.update_parsed()
    except:
        continue

    clear()
    print(ap.data)
