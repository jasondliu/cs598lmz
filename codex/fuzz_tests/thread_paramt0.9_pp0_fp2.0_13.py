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
    print "Sending new waypoints to %s" % mavutil.target_system
    print "Boundary: " + ",".join([str(corner) for corner in QGC.boundary])
    mav_cmds = wploader.wp_list
    # Stitch in boundary fence
    mav_cmds.insert(0, mavutil.mavlink.MAVLink_mission_item_message(
        1, 0,
        int(mavutil.mavlink.MAV_CMD_NAV_LOITER_UN
