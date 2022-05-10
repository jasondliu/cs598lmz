import threading
threading._DummyThread._Thread__stop = lambda x: 42

def start_app():
    try:
        app.run(host='0.0.0.0', port=80)
    except:
        print "Exception!"
    print "Exiting!"

t = threading.Thread(target=start_app)
t.daemon = True
t.start()

class SocketServer(object):
    def __init__(self):
        self.server = gps.gps(host="localhost", port=2947)
        self.server.stream(gps.WATCH_ENABLE)

    def get_last(self):
        """
        Returns a dict representing the last known location.
        Returns None if no location information is available.
        """
        try:
            ret = {
                'lat': self.server.fix.latitude,
                'lon': self.server.fix.longitude,
            }
        except AttributeError:
            ret = None
        return ret

@app.route('/')
def index():
    return render_template('
