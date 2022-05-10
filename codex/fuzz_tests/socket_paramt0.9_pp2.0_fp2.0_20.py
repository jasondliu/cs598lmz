import socket
socket.if_indextoname(3)
ifconfig
```

Edit crontab to start script on boot:

```bash
crontab -e
```

Type to insert a new cron job:
```bash
@reboot cd /home/pi/IoTMVP && sudo python run.py
```

Update the mode (i.e. `mode = 'settings'`):

```bash
nano /home/pi/IoTMVP/mqtt_to_thingspeak/constants.py
```

Issue a reboot:

```bash
sudo reboot
```

***DONE***

## Resources/Readings
About ThingSpeak
- [ThingSpeak](https://www.mathworks.com/');

About MQTT
- [MQTT](http://mqtt.org/');
- [MQTT on Wikipedia](https://en.wikipedia.org/wiki/MQTT');

About CRON
- [Cron HowTo](https://help.ubuntu.com/community/CronHowto');
- [Cron Schedule Format](
