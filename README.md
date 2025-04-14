# Environmental and Light Sensor Logger for Raspberry Pi

This script reads data from two I²C sensors — the Adafruit TSL2591 (lux/light) and AHT20 (temperature/humidity) — and logs the readings to a JSON file on an external USB drive.

## Features

- Reads:
  - Ambient temperature and humidity using the **AHT20**
  - Light intensity, infrared, and visible light using the **TSL2591**
- Appends sensor readings as JSON entries to a date-stamped file
- Automatically includes device identity from a `Node_ID.txt` file
- Designed to run on Raspberry Pi (tested on Pi Zero)

## Hardware Required

- Raspberry Pi (e.g., Pi Zero, Pi 4)
- Adafruit **TSL2591** High Dynamic Range Digital Light Sensor
- Adafruit **AHT20** Temperature and Humidity Sensor
- External USB drive mounted at `/media/pi/BEAMdrive`
- A `Node_ID.txt` file in the working directory containing the device ID

##  Libraries Required

Install the following CircuitPython libraries via `pip`:

```bash
sudo pip install adafruit-circuitpython-tsl2591 --break-system-packages
sudo pip install adafruit-circuitpython-ahtx0 --break-system-packages
