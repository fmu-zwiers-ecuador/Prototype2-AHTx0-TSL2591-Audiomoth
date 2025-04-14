import time
import board
import datetime
import adafruit_tsl2591
import adafruit_ahtx0

# Open the file with the date as its name in append mode to avoid overwriting data
file_path = "/media/pi/BEAMdrive/" + open("Node_ID.txt").read().strip() + "_" + datetime.datetime.now().strftime("%m-%d-%y") + ".json"

# Set up I2C
i2c = board.I2C()

# Declare light sensing variables
lux = -1.0
ir = -1.0
vis = -1.0
full_spec = -1.0

# Declare environmental sensing variables
temp = -1.0
hum = -1.0

# TSL2591 - Light sensor
try:
    light_sensor = adafruit_tsl2591.TSL2591(i2c)
    lux = light_sensor.lux
    ir = light_sensor.infrared
    vis = light_sensor.visible
    full_spec = light_sensor.full_spectrum
except Exception as e:
    print(f"Error reading from TSL2591: {e}")


# AHT20 - Temp & humidity sensor
try:
    temp_humidity_sensor = adafruit_ahtx0.AHTx0(i2c)
    temp = temp_humidity_sensor.temperature
    hum = temp_humidity_sensor.relative_humidity
except Exception as e:
    print(f"Error reading from AHT20: {e}")

# Write the data to the file with automatic closure
with open(file_path, "a") as file:
    file.write("{\n")
    file.write("\t\"time\": \"" + datetime.datetime.now().strftime("%H:%M:%S") + "\",\n")
    file.write("\t\"temperature\": %0.1f" % temp + ",\n")
    file.write("\t\"humidity\": %0.1f" % hum + ",\n")
    
    file.write("\t\"lux\": {}".format(lux) + ",\n")
    file.write("\t\"visible\": {}".format(vis) + ",\n")
    file.write("\t\"infrared\": {}".format(ir) + "\n")
    file.write("\t\"full-spectrum\": {}".format(full_spec) + "\n")
    file.write("}\n")
