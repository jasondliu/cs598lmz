import signal
signal.signal(signal.SIGINT, signal_handler)

ser = serial.Serial('/dev/ttyUSB0', 9600)

# http://blog.miguelgrinberg.com/post/video-streaming-with-flask

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# http://flask.pocoo.org/docs/0.10/quickstart/#a-minimal-application

@app.route("/")
def hello():
    return "Hello World!"

#http://stackoverflow.com/questions/27745765/sending-and-receiving-serial-data-
