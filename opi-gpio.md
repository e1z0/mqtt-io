
```
# works with orangepi lite
mqtt:
  host: 192.168.1.1
  client_id: mqtt-io-relay
  topic_prefix: home-relay
  ha_discovery:
    enabled: yes

# GPIO
gpio_modules:
  - name: opi
    module: orangepi
    board: pcpcplus
    mode: board

# physical pins
# 11 - upper cooler, 12 - downer cooler, 31 - outdoor lights, 32 - korridor, 33 - kitchenm, 35 - RASPBERRY CAM1-2, 36 - bedroom, 37 - workroom,

digital_outputs:
    - name: kitchen_light
      module: opi
      pin: 33
      inverted: yes
      initial: high
      publish_initial: true
      ha_discovery:
          component: switch
          name: Kitchen Light


```
