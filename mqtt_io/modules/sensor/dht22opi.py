"""
DHT22 temperature and humidity sensors for orangepi using dht22 pure lib
"""

from ...exceptions import RuntimeConfigError
from ...types import CerberusSchemaType, ConfigType, PinType, SensorValueType
from . import GenericSensor

REQUIREMENTS = ()
ALLOWED_TYPES = ["dht22"]
CONFIG_SCHEMA: CerberusSchemaType = {
    "pin": dict(type="integer", required=True, empty=False),
    "type": dict(
        type="string",
        required=True,
        empty=False,
        allowed=ALLOWED_TYPES + [x.upper() for x in ALLOWED_TYPES],
    ),
}


class Sensor(GenericSensor):
    """
    Implementation of Sensor class for the DHT22 temperature sensor.
    """

    SENSOR_SCHEMA: CerberusSchemaType = {
        "type": dict(
            type="string",
            required=False,
            empty=False,
            default="temperature",
            allowed=["temperature", "humidity"],
        )
    }

    def setup_module(self) -> None:
        # pylint: disable=import-outside-toplevel,import-error
        import dhtopi as DHTsensor
        from pyA20.gpio import gpio as gipis

        sensor_type: str = self.config["type"].lower()

        self.sensor_type: int
        if sensor_type == "dht22":
            self.sensor_type = "dht22"
        else:
            raise RuntimeConfigError("Supported sensor types: DHT22")

        self.pin: PinType = self.config["pin"]
        gipis.init()
        sen = DHTsensor.DHT(pin=self.pin)
        self.sensor = sen.read()

    def get_value(self, sens_conf: ConfigType) -> SensorValueType:
        """
        Get the temperature or humidity value from the sensor
        """
        humidity: SensorValueType
        temperature: SensorValueType
        if self.sensor.is_valid():
         if sens_conf["type"] == "temperature":
           return self.sensor.temperature
         if sens_conf["type"] == "humidity":
            return self.sensor.humidity
         raise RuntimeConfigError(
            "dht22 sensor '%s' was not configured to return 'temperature' or 'humidity'"
              % sens_conf["name"])
        raise ("Just give it a little bit relax :-)")
