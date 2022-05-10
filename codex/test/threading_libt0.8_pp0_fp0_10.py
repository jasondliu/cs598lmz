import threading
threading.Thread( None , decode ,args =( "http://localhost:3000/video_feed", ) ).start()

from client import send
send()
