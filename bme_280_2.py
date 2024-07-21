import bme280
import smbus2
from time import sleep

# adding comment

port = 1
address = 0x76  # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)

for reading in range(5):
    bme280_data = bme280.sample(bus, address)
    humidity = bme280_data.humidity
    pressure = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    out_msg = f"""Humedad actua: {humidity}
                Presion actual: {pressure}
                Temperatura: {ambient_temperature} C"""
    print(ambient_temperature)
    sleep(1)
