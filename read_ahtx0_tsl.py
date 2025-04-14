import time
import board
import adafruit_tsl2591
import adafruit_ahtx0

# Set up I2C
i2c = board.I2C()

# Initialize sensors
light_sensor = adafruit_tsl2591.TSL2591(i2c)
temp_humidity_sensor = adafruit_ahtx0.AHTx0(i2c)

# Main loop
while True:
    # TSL2591 - Light sensor
    lux = light_sensor.lux
    infrared = light_sensor.infrared
    visible = light_sensor.visible
    full_spectrum = light_sensor.full_spectrum

    print("\nLight Sensor Readings:")
    print("  Total light: {:.2f} lux".format(lux))
    print("  Infrared light: {}".format(infrared))
    print("  Visible light: {}".format(visible))
    print("  Full spectrum (IR + visible): {}".format(full_spectrum))

    # AHT20 - Temp & humidity sensor
    temperature = temp_humidity_sensor.temperature
    humidity = temp_humidity_sensor.relative_humidity

    print("Temperature: {:.1f}°C".format(temperature))
    print("Humidity: {:.1f}%".format(humidity))

    time.sleep(2)
