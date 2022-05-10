import ctypes
ctypes.windll.user32.MessageBoxW(0, "Running at %f Frames Per Second" % camera.frame_rate, "FPS", 1)
           
#camera.recording = True
camera.recording = False
try:
    for frame in camera:
        #camera.stream
        #camera.start_recording(camera.stream)
        frame = frame[0]
        #frame = cv2.flip(frame, 1)
        frame = numpy.rot90(frame)
        print('Type: ' + str(type(frame)))
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame, 1)
        if not camera.recording:
            frame = cv2.rectangle(frame, (640, 20), (700, 80), (255, 0, 0), -1)
        else:
            frame = cv2.rectangle(
