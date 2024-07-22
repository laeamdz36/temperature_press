from flask import Flask
import bme280
import smbus2

app = Flask(__name__)


def get_data():
    """Get data from sensor"""
    port = 1
    address = 0x76  # Adafruit BME280 address. Other BME280s may be different
    bus = smbus2.SMBus(port)

    bme280.load_calibration_params(bus, address)

    bme280_data = bme280.sample(bus, address)
    humidity = f"Humedad actual: {bme280_data.humidity:.2f} %"
    pressure = f"Presion actual: {bme280_data.pressure:.2f} hPa"
    ambient_temperature = f"Temperatura: {bme280_data.temperature:.2f} °C"

    return humidity, pressure, ambient_temperature


@app.route("/")
def index():
    """Index page"""
    return "Hello world"


@app.route("/testing")
def testing():
    """Testing"""
    return "testing"


@app.route("/temperature")
def temperature():
    """Show temperature info"""
    humidity, pressure, ambient_temperature = get_data()
    return humidity, pressure, ambient_temperature


if __name__ == "__main__":
    app.run(host="0.0.0.0")
