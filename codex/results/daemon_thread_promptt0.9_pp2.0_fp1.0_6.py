import threading
# Test threading daemon. This deamon should run for 60 seconds.
def daemon():
    print('Daemon starting.')
    time.sleep(20)
    print('Daemon exiting.')
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
d.start()

d.isActive()

WEATHER_KEY = 'b865c02264fb5da5e5a5febdf5c5d3a3'

ACCu_KEY = '1aM0iYYZKwAnb582Cxvx8SpmyEKgXkRp'


city = 'London'
try:
    
    weather = requests.get("http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}".format(city, WEATHER_KEY))
    weather = weather.json()

    #print(weather['list'])
    #print(weather['list'][0]['weather'][0]['description'], weather['list'][0]['main']['
