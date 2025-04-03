#!/usr/bin/env python3

import board
import busio
import time
import adafruit_ahtx0
import adafruit_tsl2591
import datetime
import json

# Setup I2C for both sensors
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize AHT20 for temperature & humidity
try:
    aht = adafruit_ahtx0.AHTx0(i2c)
    temperature = round(aht.temperature, 1)
    humidity = round(aht.relative_humidity, 1)
except Exception as e:
    print(f"Error reading AHT20: {e}")
    temperature = None
    humidity = None

# Initialize TSL2591 for light sensing
lux = None
ir = None
vis = None
try:
    tsl = adafruit_tsl2591.TSL2591(i2c)
    lux = tsl.lux
    ir = tsl.infrared
    broadband = tsl.broadband
    vis = broadband - ir
except Exception as e:
    print(f"Error reading TSL2591: {e}")

# Get time and file path
timestamp = datetime.datetime.now().strftime("%H:%M:%S")
try:
    with open("Node_ID", "r") as f:
        node_id = f.read().strip()
except Exception:
    node_id = "UnknownNode"

file_path = f"/media/pi/BEAMdrive/{node_id}: {datetime.datetime.now().strftime('%m-%d-%y')}.json"

# Prepare data dictionary
data = {
    "time": timestamp,
    "temperature": temperature,
    "humidity": humidity,
    "lux": lux,
    "visible": vis,
    "infrared": ir
}

# Write data to JSON file
try:
    with open(file_path, "a") as file:
        json.dump(data, file)
        file.write("\n")
except Exception as e:
    print(f"Error writing to file: {e}")