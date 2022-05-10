import signal
signal.signal(signal.SIGINT, signal_handler)

# Create PiCamera object
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

# Initialize camera
time.sleep(.1)
camera.start_preview()

# Create stream object
stream = io.BytesIO()

# Continuously capture frames from PiCamera and send to GStreamer pipe
for foo in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
    # Rewind the stream for reading
    stream.seek(0)

    # Construct numpy array and send to GStreamer pipeline
    send_image(stream)

    # Reset stream for next capture
    stream.seek(0)
    stream.truncate()

    # Check if thread is stopped
    if not running:
        break

# Clean up thread
print('Stopping PiCamera')
camera.stop_preview()
camera.close()
