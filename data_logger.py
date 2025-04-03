import time
import board
import json
from datetime import datetime

# Power and battery
import adafruit_ina260
from adafruit_lc709203f import LC709203F

# Environmental sensors
import adafruit_tsl2591
import adafruit_ahtx0

# Initialize I2C
i2c = board.I2C()

# Power sensor (INA260)
ina260 = adafruit_ina260.INA260(i2c)

# Battery fuel gauge (LC709203F)
battery_sensor = LC709203F(i2c)

# Light sensor (TSL2591)
light_sensor = adafruit_tsl2591.TSL2591(i2c)

# Temp & Humidity sensor (AHT20)
aht_sensor = adafruit_ahtx0.AHTx0(i2c)

json_file_path = "/home/pi/full_data.json"  # Change to USB if needed

# Load existing data if file exists
try:
    with open(json_file_path, "r") as f:
        data_log = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data_log = []

while True:
    try:
        timestamp = datetime.now().isoformat()

        # Power and battery
        current = ina260.current
        voltage = ina260.voltage
        power = ina260.power
        cell_voltage = battery_sensor.cell_voltage
        battery_percent = battery_sensor.cell_percent

        # Light
        lux = light_sensor.lux

        # Temperature and humidity
        temperature = aht_sensor.temperature
        humidity = aht_sensor.relative_humidity

        data_entry = {
            "timestamp": timestamp,
            "ina260": {
                "current_mA": round(current, 2),
                "voltage_V": round(voltage, 2),
                "power_mW": round(power, 2)
            },
            "lc709203f": {
                "cell_voltage_V": round(cell_voltage, 3),
                "battery_percent": round(battery_percent, 1)
            },
            "aht20": {
                "temperature_C": round(temperature, 2),
                "humidity_percent": round(humidity, 2)
            },
            "tsl2591": {
                "lux": round(lux, 2)
            }
        }

        data_log.append(data_entry)

        # Write to JSON file
        with open(json_file_path, "w") as f:
            json.dump(data_log, f, indent=4)

        print(f"[{timestamp}] Logged successfully")

    except OSError:
        print("Sensor read failed — retrying after delay...")

    time.sleep(300)  # Wait 5 minutes
