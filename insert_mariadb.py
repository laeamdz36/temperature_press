"""Insert into maria db data fot reading BME280"""
import bme280
import smbus2
import mariadb
import datetime as dt


def read_bme_data():
    """Read data from BME sensor"""

    port = 1
    address = 0x76  # Adafruit BME280 address. Other BME280s may be different
    bus = smbus2.SMBus(port)

    bme280.load_calibration_params(bus, address)

    bme280_data = bme280.sample(bus, address)
    humidity = f"Humedad actual: {bme280_data.humidity} %"
    pressure = f"Presion actual: {bme280_data.pressure} hPa"
    ambient_temperature = f"Temperatura: {bme280_data.temperature} °C"

    return humidity, pressure, ambient_temperature
