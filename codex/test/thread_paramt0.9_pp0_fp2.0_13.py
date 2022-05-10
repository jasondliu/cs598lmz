import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()

def cmd_callback(data):
    global mavutil
    print(data.data) 
    mavutil.mav.mission_request_send(mavutil.target_system, mavutil.target_component, int(data.data))

def send_waypoints(wp_file):
    global mavutil, QGC
    wploader = mavwp.MAVWPLoader()
    wploader.load(wp_file)
