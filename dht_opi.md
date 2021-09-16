# OrangePI dht22 support

Install python 3.9 from source and continue installing required parts
```
pip3 install pyA20
wget https://raw.githubusercontent.com/jingl3s/DHT11-DHT22-Python-library-Orange-PI/master/dht.py
cp dht.py /usr/local/lib/python3.9/dhtopi.py
cp mqtt_io/modules/sensor/dht22opi.py /usr/local/lib/python3.9/site-packages/mqtt_io/modules/sensor/
```
