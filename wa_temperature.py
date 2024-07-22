from flask import Flask, render_template

# app = Flask(__name__)
app = Flask(__name__, template_folder='templates')


def get_data():
    """Get data from sensor"""
    import bme280
    import smbus2
    port = 1
    address = 0x76  # Adafruit BME280 address. Other BME280s may be different
    bus = smbus2.SMBus(port)

    bme280.load_calibration_params(bus, address)

    bme280_data = bme280.sample(bus, address)
    humidity = f"Humedad actual: {bme280_data.humidity:.2f} %"
    pressure = f"Presion actual: {bme280_data.pressure:.2f} hPa"
    ambient_temperature = f"Temperatura: {bme280_data.temperature:.2f} °C"
    total_msg = humidity + "\n" + pressure + "\n" + ambient_temperature

    return total_msg


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
    total_msg = get_data()
    return render_template("temperature.html", temp_info=total_msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
