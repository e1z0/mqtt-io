# OrangePI dht22 support

Install python 3.9 from source and continue installing required parts
```
pip3 install pyA20
wget https://raw.githubusercontent.com/jingl3s/DHT11-DHT22-Python-library-Orange-PI/master/dht.py
cp dht.py /usr/local/lib/python3.9/dhtopi.py
cp mqtt_io/modules/sensor/dht22opi.py /usr/local/lib/python3.9/site-packages/mqtt_io/modules/sensor/
```

Config

```
# Sensors
sensor_modules:
  - name: dht
    module: dht22opi
    type: DHT22
    pin: 21 # bcm type of port

sensor_inputs:
  - name: bath_temp
    module: dht
    type: temperature
    interval: 10
  - name: bath_humidity
    module: dht
    type: humidity
    interval: 10
```
