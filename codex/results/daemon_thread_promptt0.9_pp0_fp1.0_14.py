import threading
# Test threading daemon
def daemon_mode(main_func, return_val=None, t_sleep=5, t_name="daemon_mode"):
    t = threading.Thread(target=main_func, args=(return_val,), name=t_name)
    t.setDaemon(True)
    t.start()
    # time.sleep(t_sleep)

# Calculate distance between two points X1 and X2
def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  

# Check if point exist in the list
def check_point(point, group_point):
    flag = False
    for key, val in group_point.items():
        if key == point:
            flag = True
    return flag

# Find two farthest points
def find_two_farthest_points(group_point):
    if len(group_point) == 2:
        max_dist = calculateDistance(group_
