import threading
# Test threading daemon
# import time

# def daemon():
#     print('start daemon')
#     time.sleep(10)
#     print('stop daemon')

# d = threading.Thread(target=daemon)
# d.setDaemon(True)
# d.start()

# AppDaemon
url = 'http://localhost:8090'
headers = {
    "Accept" : "application/json",
    "x-ha-access": "password"
}

# Test AppDaemon ok
# r = requests.get(url, headers=headers)
# print(r.status_code)
# print(r)

url = 'http://localhost:8090/states/sensor.bosch_sensor'

# Test get data
# r = requests.get(url, headers=headers)
# print(r.text)

# Test data format
# h = ast.literal_eval(r.text)
# print(h)

# Value need
# state = h['state']
# unit = h['attributes']['unit_of_
