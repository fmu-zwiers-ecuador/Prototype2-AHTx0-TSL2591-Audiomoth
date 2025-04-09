import time
import board
import digitalio
import adafruit_tsl2591
import datetime
# Setup I2C for both sensors
i2c = busio.I2C(board.SCL, board.SDA)

# Open the file with the date as its name in append mode to avoid overwriting data
file_path = "/media/pi/BEAMdrive/" + open("Node_ID.txt").read().strip() + "_" + datetime.datetime.now().strftime("%m-%d-%y") + ".json"

# Declare environmental sensing variables
hum = -1.0
temp = -1.0

# Initialize AHT20 for temperature & humidity
try:
    aht = adafruit_ahtx0.AHTx0(i2c)
    temperature = round(aht.temperature, 1)
    humidity = round(aht.relative_humidity, 1)
except Exception as e:
    print(f"Error reading AHT20: {e}")
    temperature = None
    humidity = None


cs = digitalio.DigitalInOut(board.D5)
spi = board.SPI()
i2c = board.I2C()


# Declare light sensing variables
lux = -1.0
ir = -1.0
vis = -1.0
full_spec = -1.0


try:
    sensor = adafruit_tsl2591.TSL2591(i2c)
    lux = sensor.lux
    ir = sensor.infrared
    vis = sensor.visible
    full_spec = sensor.full_spectrum
except Exception as e:
    print(f"Error reading from TSL2561: {e}")


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
