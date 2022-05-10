import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

###############     Motor Code     ###############
def motor_controls(x, y):
    if (target_state == 0):
        # Manual drive
        r_speed = (y - x) * power_gain
        l_speed = (y + x) * power_gain
    else:
        # Autonomous drive
        r_speed = -x * power_gain
        l_speed = -y * power_gain

    m_left.run(Adafruit_MotorHAT.FORWARD)
    m_right.run(Adafruit_MotorHAT.FORWARD)

    if (r_speed == 0):
        m_right.run(Adafruit_MotorHAT.RELEASE)
    elif (r_speed > 0):
        m_right.setSpeed(r_speed)
    else:
        m_right.run(Adafruit_MotorHAT.BACKWARD)
        m_right.setSpeed(r_speed * -1)

    if (l_speed == 0):
       
