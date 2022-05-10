import signal
signal.signal(signal.SIGINT, lambda s, f: sys.exit(0))

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
                    help="The ip to listen on")
parser.add_argument("--port", type=int, default=8080,
                    help="The port to listen on")
parser.add_argument("--chunk-size", type=int, default=1,
                    help="Chunk size to use in bytes")
args = parser.parse_args()

@app.route('/')
def index():
    """Video streaming home page. """
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    # print "Starting generator"
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


