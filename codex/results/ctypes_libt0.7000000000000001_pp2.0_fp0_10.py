import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

def get_battery_status():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    status = 'Plugged in' if plugged else 'Discharging'
    battery_status = percent, status

    return battery_status

def get_battery_percentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    return percent

def get_battery_plugged():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    if plugged:
        status = 'Plugged in'
    else:
        status = 'Discharging'
    return status

def get_wifi_status():
    try:
        adapter = wmi.WMI(namespace="wlanapi").WlanClient()
        interface = adapter.connections[0]
        return interface.get_properties()['profileName']
    except:
