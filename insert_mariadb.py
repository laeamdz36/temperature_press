"""Insert into maria db data fot reading BME280"""
import sys
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


def read_bme_data_v1():
    """Read data from BME sensor"""

    port = 1
    address = 0x76  # Adafruit BME280 address. Other BME280s may be different
    bus = smbus2.SMBus(port)

    bme280.load_calibration_params(bus, address)

    bme280_data = bme280.sample(bus, address)
    humidity = float(bme280_data.humidity)
    pressure = float(bme280_data.pressure)
    ambient_temperature = float(bme280_data.temperature)

    return humidity, pressure, ambient_temperature


def mariadb_conn():
    """Connection to database mariadb verify file"""

    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user="raspi_1",
            password="luismdz36",
            host="192.168.0.20",
            port=3306,
            database="temperature_data")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cursor = conn.cursor()

    conn.close()


def mariadb_conn_v1():
    """Connection to database mariadb"""

    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user="raspi_1",
            password="luismdz36",
            host="localhost",
            port=3306,
            database="temperature_data")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cursor = conn.cursor()

    return cursor


def insert_into_db():
    """Insert into de database for temperature, humidity and pressure"""
    humidity, pressure, temp = read_bme_data_v1()
    # DB connection
    cur = mariadb_conn_v1()
    date = dt.datetime.today()
    # insert information
    try:
        cur.execute(
            "INSERT INTO data_temp (date_time, temperature, humidity, pressure) VALUES (?, ?, ?, ?)", (date, temp, humidity, pressure))
    except mariadb.Error as e:
        print(f"Error: {e}")
    cur.close()


if __name__ == "__main__":
    insert_into_db()
